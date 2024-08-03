import boto3
from constants import SNS_TOPIC_ARN


def request_to_sns(message: str):
    """
    Publishes a message to an SNS topic.

    This function sends a message to an Amazon SNS topic specified by the `SNS_TOPIC_ARN` constant. It uses
    the `boto3` SNS client to perform the publish operation.

    Parameters:
        message (str): The message to be sent to the SNS topic.

    Returns:
        dict: The response from the `publish` operation, which includes details about the published message.

    Example:
        >>> request_to_sns("Sale processed successfully.")
        {
            'MessageId': 'some-message-id',
            'ResponseMetadata': {
                'RequestId': 'some-request-id',
                'HTTPStatusCode': 200,
                'HTTPHeaders': { ... },
                'RetryAttempts': 0
            }
        }
    """
    client = boto3.client("sns")
    return client.publish(
        TopicArn=SNS_TOPIC_ARN,
        Subject="Status Sale",
        Message=message,
    )
