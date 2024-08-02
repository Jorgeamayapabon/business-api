import json
import boto3


def request_to_sqs_fifo(
    queue_item: dict,
    region_name: str,
    queue_name: str,
    message_group_id: str,
):
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
