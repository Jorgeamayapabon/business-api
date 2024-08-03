import boto3


def db_insert(table_name: str, item: dict) -> int:
    """
    Inserts an item into a DynamoDB table.

    This function attempts to insert a specified item into a DynamoDB table and returns the HTTP status code
    indicating the result of the operation.

    Parameters:
        table_name (str): The name of the DynamoDB table where the item will be inserted.
        item (dict): The item to be inserted into the table. The item should conform to the schema expected
                     by the DynamoDB table.

    Returns:
        int: The HTTP status code resulting from the insertion. Returns 200 if successful, otherwise 500
             if an exception occurs.

    Example:
        >>> db_insert("my_table", {"id": "123", "name": "Alice"})
        200
    """
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
