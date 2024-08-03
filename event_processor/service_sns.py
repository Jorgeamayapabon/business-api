import boto3
from constants import SNS_TOPIC_ARN


def request_to_sns(message: str):
    """
    Publishes a message to an Amazon SNS topic.

    This function sends a message to a specified Amazon Simple Notification Service (SNS) topic.
    The message is published with a subject of "Status Sale". 

    Parameters:
        message (str): The message content to publish to the SNS topic.

    Returns:
        dict: The response from the SNS publish operation. It includes metadata about the message publishing.

    Raises:
        boto3.exceptions.Boto3Error: If there is an error with the SNS client or the publish operation.

    Examples:
        >>> request_to_sns("Sale processed successfully")
        {'MessageId': 'abcd1234-5678-90ab-cdef-1234567890ab'}
    """
    client = boto3.client("sns")
    return client.publish(
        TopicArn=SNS_TOPIC_ARN,
        Subject="Status Sale",
        Message=message,
    )
