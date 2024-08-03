import boto3


def event_bridge_put_event(
    source: str,
    detail: str,
    detail_type: str,
) -> dict:
    """
    Sends an event to AWS EventBridge.

    This function sends a custom event to the AWS EventBridge using the provided 
    source, detail, and detail type. The event is sent to the default event bus.

    Parameters:
        source (str): The source of the event (e.g., an application name or service).
        detail (str): The detail of the event, provided as a JSON-formatted string.
        detail_type (str): The type of the event detail, which helps categorize the event.

    Returns:
        dict: The response from the AWS EventBridge `put_events` API call.

    Raises:
        botocore.exceptions.ClientError: If there is an error with the EventBridge client or the event submission.

    Examples:
        >>> event_bridge_put_event(
        ...     source="my.application",
        ...     detail=json.dumps({"key": "value"}),
        ...     detail_type="MyEventType"
        ... )
        {'FailedEntryCount': 0, 'Entries': [{'EventId': '12345678-1234-1234-1234-123456789012'}]}
    """
    client = boto3.client("events")
    return client.put_events(
        Entries=[
            {
                "Source": source,
                "DetailType": detail_type,
                "Detail": detail,
                "EventBusName": "default",
            },
        ]
    )
