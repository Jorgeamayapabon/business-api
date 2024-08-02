import boto3


def db_consult(table_name: str, key_name: str, key_value: str):
    try:
        dynamo = boto3.resource("dynamodb")
        table = dynamo.Table(table_name)

        response = table.get_item(Key={key_name: key_value})

        return response["Item"]

    except Exception as e:
        print(f"Exception in db_consult: {e}")
        return {}


def db_insert(table_name: str, item: dict):
    try:
        http_status_code = 400
        dynamo = boto3.resource("dynamodb")
        table = dynamo.Table(table_name)

        response = table.put_item(Item=item)

        http_status_code = response["ResponseMetadata"]["HTTPStatusCode"]
        print(f"http_status_code in db_insert => {http_status_code}")

        return http_status_code

    except Exception as e:
        response = str(e)
        print(f"exception in db_insert => {response}")

        return 500


def db_delete(
    table_name: str, 
    key_name: str, 
    key_value: str
):
    try:
        http_status_code = 400
        dynamo = boto3.resource("dynamodb")
        table = dynamo.Table(table_name)
        response = table.delete_item(
            Key={key_name: key_value},
        )
        http_status_code = response['ResponseMetadata']['HTTPStatusCode']

        return http_status_code
    except Exception as e:
        response = str(e)
        print(f'exception in db_delete => {response}')
        
        return 500
