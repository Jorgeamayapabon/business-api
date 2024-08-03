import json
import boto3


def request_to_sqs_fifo(
    queue_item: dict,
    region_name: str,
    queue_name: str,
    message_group_id: str,
):
    """
    Sends a message to an AWS SQS FIFO queue.

    This function sends a JSON-serialized message to a specified FIFO SQS queue
    in the given AWS region. It uses the `message_group_id` to group messages
    within the queue.

    Parameters:
        queue_item (dict): The message payload to send to the queue.
        region_name (str): The AWS region where the SQS queue is located.
        queue_name (str): The name of the SQS FIFO queue.
        message_group_id (str): The message group ID for the message.

    Returns:
        None

    Raises:
        botocore.exceptions.ClientError: If there is an error with the SQS client or the queue operation.

    Examples:
        >>> request_to_sqs_fifo(
        ...     queue_item={"order_id": "12345", "status": "pending"},
        ...     region_name="us-west-2",
        ...     queue_name="my-fifo-queue.fifo",
        ...     message_group_id="order-group"
        ... )
    """
    # Crear un cliente SQS
    sqs = boto3.client('sqs', region_name=region_name)

    # Obtener la URL de la cola
    response = sqs.get_queue_url(QueueName=queue_name)
    queue_url = response['QueueUrl']

    # Enviar un mensaje a la cola
    sqs.send_message(
        QueueUrl=queue_url,
        MessageBody=json.dumps(queue_item),
        MessageGroupId=str(message_group_id),
    )
