import boto3


def event_bridge_put_event(
    source: str,
    detail: str,
    detail_type: str,
) -> dict:
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
