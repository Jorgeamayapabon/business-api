import json
from service_sns import request_to_sns
from constants import MESSAGE_CLIENT_UPDATED


def lambda_handler(event, context):
    print(event)
    
    request_to_sns(message=MESSAGE_CLIENT_UPDATED)
        
    return {
        "statusCode": 200,
        "body": json.dumps({"message": "OK"}),
    }
