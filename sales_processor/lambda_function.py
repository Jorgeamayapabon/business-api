import json
from base_models import RecordsEvent
from query_templates import create_sale
from service_sns import request_to_sns
from constants import MESSAGE_SALE_NOT_PROCESSED


def lambda_handler(event, context):
    """
    AWS Lambda function handler to process sale records.

    This function processes incoming events, extracts sale, user, and client information from the records,
    and attempts to create a sale record in the database. It sends notifications via SNS based on the
    success or failure of the sale processing.

    Parameters:
        event (dict): The event data passed to the Lambda function. Expected to conform to the RecordsEvent model.
        context (object): The context object provided by AWS Lambda, containing metadata about the invocation.

    Returns:
        dict: The HTTP response with status code and message indicating the result of the processing.

    Raises:
        Exception: If an error occurs during processing, it sends a notification and returns a 200 response.
    """
    try:
        print(event)

        records = RecordsEvent(**event)
        body = records.Records[0].body
        sale = body.sale
        user = body.user
        client = body.client

        status = create_sale(sale_item=sale.model_dump())

        if status != 200:
            request_to_sns(message=MESSAGE_SALE_NOT_PROCESSED)

        message = (
            "Sale processed successfully.\n\n"
            + f"User: {user.fullname}\n"
            + f"Client: {client.fullname}\n"
            + f"Value: {sale.value}\n"
        )

        request_to_sns(message=message)

    except Exception:
        request_to_sns(message=MESSAGE_SALE_NOT_PROCESSED)

    return {
        "statusCode": 200,
        "body": json.dumps({"message": "OK"}),
    }
