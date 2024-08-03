import json
from service_sns import request_to_sns
from constants import MESSAGE_CLIENT_UPDATED


def lambda_handler(event, context):
    """
    AWS Lambda function handler for processing events and publishing messages to SNS.

    This Lambda function processes incoming events, prints the event to the logs, and sends a predefined
    message to an Amazon SNS topic using the `request_to_sns` function. It then returns a response with a
    status code of 200 and a JSON body indicating success.

    Parameters:
        event (dict): The event data passed to the Lambda function. The content of this event is printed 
                      to the logs for debugging purposes.
        context (object): The context object provides runtime information (e.g., function name, version).

    Returns:
        dict: A response with a status code of 200 and a JSON body containing a success message.

    Raises:
        boto3.exceptions.Boto3Error: If there is an error with the SNS client or the publish operation.
    """
    print(event)
    
    request_to_sns(message=MESSAGE_CLIENT_UPDATED)
        
    return {
        "statusCode": 200,
        "body": json.dumps({"message": "OK"}),
    }
