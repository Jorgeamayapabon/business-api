import boto3


def db_consult(table_name: str, key_name: str, key_value: str):
    """
    Retrieves an item from a DynamoDB table.

    This function queries a DynamoDB table for an item based on the specified 
    key name and key value. It returns the item if found, or an empty dictionary 
    if an error occurs or if the item is not found.

    Parameters:
        table_name (str): The name of the DynamoDB table.
        key_name (str): The primary key name for the item in the table.
        key_value (str): The value of the primary key for the item to retrieve.

    Returns:
        dict: The item retrieved from the table, or an empty dictionary if an error occurs or the item is not found.

    Raises:
        botocore.exceptions.ClientError: If there is an error with the DynamoDB client or the query operation.

    Examples:
        >>> db_consult("UsersTable", "user_id", "12345")
        {'user_id': '12345', 'fullname': 'John Doe', 'email': 'john.doe@example.com'}
        
        >>> db_consult("UsersTable", "user_id", "99999")
        {}
    """
    try:
        dynamo = boto3.resource("dynamodb")
        table = dynamo.Table(table_name)

        response = table.get_item(Key={key_name: key_value})

        return response["Item"]

    except Exception as e:
        print(f"Exception in db_consult: {e}")
        return {}


def db_insert(table_name: str, item: dict):
    """
    Inserts an item into a DynamoDB table.

    This function adds an item to the specified DynamoDB table and returns
    the HTTP status code of the operation. If the insertion is successful,
    it returns the status code 200. If an error occurs, it returns 500.

    Parameters:
        table_name (str): The name of the DynamoDB table to insert the item into.
        item (dict): The item to insert into the table. The item must be a dictionary where 
                     the keys correspond to the table's attributes.

    Returns:
        int: The HTTP status code of the operation. 200 for success, 500 for an error.

    Raises:
        botocore.exceptions.ClientError: If there is an error with the DynamoDB client or the insertion operation.

    Examples:
        >>> db_insert("UsersTable", {"user_id": "12345", "fullname": "John Doe", "email": "john.doe@example.com"})
        200

        >>> db_insert("UsersTable", {"user_id": "12345", "fullname": "Jane Smith"})
        500
    """
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
    """
    Deletes an item from a DynamoDB table.

    This function removes an item from the specified DynamoDB table based on the 
    provided key name and key value. It returns the HTTP status code of the operation.
    A successful deletion returns 200, while an error returns 500.

    Parameters:
        table_name (str): The name of the DynamoDB table from which to delete the item.
        key_name (str): The name of the key for the item to delete.
        key_value (str): The value of the key for the item to delete.

    Returns:
        int: The HTTP status code of the operation. 200 for success, 500 for an error.

    Raises:
        botocore.exceptions.ClientError: If there is an error with the DynamoDB client or the delete operation.

    Examples:
        >>> db_delete("UsersTable", "user_id", "12345")
        200
        
        >>> db_delete("UsersTable", "user_id", "99999")
        500
    """
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
