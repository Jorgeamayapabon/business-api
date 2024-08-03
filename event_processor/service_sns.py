import boto3
from constants import SNS_TOPIC_ARN


def request_to_sns(message: str):
    client = boto3.client("sns")
    return client.publish(
        TopicArn=SNS_TOPIC_ARN,
        Subject="Status Sale",
        Message=message,
    )
