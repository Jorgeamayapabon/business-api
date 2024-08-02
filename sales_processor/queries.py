import boto3


def db_insert(table_name: str, item: dict) -> int:
    try:
        http_status_code = 400
        dynamo = boto3.resource("dynamodb")
        table = dynamo.Table(table_name)

        response = table.put_item(Item=item)

        http_status_code: int = response["ResponseMetadata"]["HTTPStatusCode"]
        print(f"http_status_code in db_insert => {http_status_code}")

        return http_status_code

    except Exception as e:
        response = str(e)
        print(f"exception in db_insert => {response}")

        return 500
