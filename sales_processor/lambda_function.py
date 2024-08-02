import json
from base_models import RecordsEvent
from query_templates import create_sale
from service_sns import request_to_sns
from constants import MESSAGE_SALE_NOT_PROCESSED


def lambda_handler(event, context):
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
        
        message = "Sale processed successfully." + \
                  f"\nUser: {user.name}" + \
                  f"\nClient: {client.name}" + \
                  f"\nValue: {sale.value}"
        request_to_sns(message=message)

    except Exception:
        request_to_sns(message=MESSAGE_SALE_NOT_PROCESSED)
        
    return {
        "statusCode": 200,
        "body": json.dumps({"message": "OK"}),
    }
