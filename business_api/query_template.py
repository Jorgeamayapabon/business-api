from base_models import Client, Sale, User
from service_event import event_bridge_put_event
from service_sqs import request_to_sqs_fifo
from constants import (
    AWS_REGION,
    MESSAGE_FAIL_CREATE_STR,
    MESSAGE_404_CLIENT_STR,
    MESSAGE_404_SALE_STR,
    MESSAGE_404_USER_STR,
    MESSAGE_FAIL_DELETE_STR,
    MESSAGE_FAIL_UPDATE_STR,
    MESSAGE_PROCESSING_SALE_STR,
    QUEUE_SALE_PROCESSOR,
    TABLE_CLIENT,
    TABLE_SALE,
    TABLE_USER,
)
from query import db_consult, db_delete, db_insert


def create_user(body: dict):
    """
    Creates a new user record in the database.

    This function takes a dictionary containing user data, validates it,
    and inserts it into the database. It returns an appropriate status code
    and message based on the success or failure of the operation.

    Parameters:
        body (dict): The data for the new user.

    Returns:
        dict: A dictionary containing the HTTP status code and a message.
    """
    try:
        user = db_consult(
            table_name=TABLE_USER, key_name="user_id", key_value=str(body["user_id"])
        )

        if user:
            return {
                "statusCode": 409,
                "body": f"user_id -{body['user_id']}- already exists",
            }

        user_item = User(**body).model_dump()

        status = db_insert(table_name=TABLE_USER, item=user_item)

        if status != 200:
            return {"statusCode": status, "body": MESSAGE_FAIL_CREATE_STR}

        return {"statusCode": 200, "body": user_item}

    except Exception as e:
        return {"statusCode": 500, "body": f"Error in create_user: {e}"}


def create_client(body: dict):
    """
    Creates a new client record in the database.

    This function takes a dictionary containing client data, validates it,
    and inserts it into the database. It returns an appropriate status code
    and message based on the success or failure of the operation.

    Parameters:
        body (dict): The data for the new client.

    Returns:
        dict: A dictionary containing the HTTP status code and a message.
    """
    try:
        client = db_consult(
            table_name=TABLE_CLIENT,
            key_name="client_id",
            key_value=str(body["client_id"]),
        )

        if client:
            return {
                "statusCode": 409,
                "body": f"client_id -{body['client_id']}- already exists",
            }

        client_item = Client(**body).model_dump()

        status = db_insert(table_name=TABLE_CLIENT, item=client_item)

        if status != 200:
            return {"statusCode": status, "body": MESSAGE_FAIL_CREATE_STR}

        return {"statusCode": 200, "body": client_item}

    except Exception as e:
        return {"statusCode": 500, "body": f"Error in create_client: {e}"}


def create_sale(body: dict):
    """
    Creates a new sale record in the database.

    This function takes a dictionary containing sale data, validates it,
    and inserts it into the database. It returns an appropriate status code
    and message based on the success or failure of the operation.

    Parameters:
        body (dict): The data for the new sale.

    Returns:
        dict: A dictionary containing the HTTP status code and a message.
    """
    try:
        sale = db_consult(
            table_name=TABLE_SALE, key_name="sale_id", key_value=str(body["sale_id"])
        )

        if sale:
            return {
                "statusCode": 409,
                "body": f"sale_id -{body['sale_id']}- already exists",
            }

        sale_item = Sale(**body).model_dump()

        user = db_consult(
            table_name=TABLE_USER, key_name="user_id", key_value=str(body["user_id"])
        )
        user_item = User(**user)

        client = db_consult(
            table_name=TABLE_CLIENT,
            key_name="client_id",
            key_value=str(body["client_id"]),
        )
        client_item = Client(**client)

        queue_item = {
            "user": user_item.model_dump(),
            "client": client_item.model_dump(),
            "sale": sale_item,
        }

        request_to_sqs_fifo(
            message_group_id=user_item.user_id,
            queue_item=queue_item,
            region_name=AWS_REGION,
            queue_name=QUEUE_SALE_PROCESSOR,
        )

        return {"statusCode": 200, "body": MESSAGE_PROCESSING_SALE_STR}

    except Exception as e:
        return {"statusCode": 500, "body": f"Error in create_sale: {e}"}


def retrieve_user(user_id: str):
    """
    Retrieves user information from the database.

    This function queries the database to find a user by their user ID.
    It returns the user data if found, or an appropriate error message
    if the user is not found or if an error occurs during the query.

    Parameters:
        user_id (str): The ID of the user to retrieve.

    Returns:
        dict: A dictionary containing the HTTP status code and either
              the user data or an error message.
    """
    try:
        user = db_consult(table_name=TABLE_USER, key_name="user_id", key_value=str(user_id))

        if user:
            return {"statusCode": 200, "body": user}

        return {"statusCode": 404, "body": MESSAGE_404_USER_STR}

    except Exception as e:
        return {"statusCode": 500, "body": f"Error in retrieve_user: {e}"}


def retrieve_client(client_id: str):
    """
    Retrieves client information from the database.

    This function queries the database to find a client by their client ID.
    It returns the client data if found, or an appropriate error message
    if the client is not found or if an error occurs during the query.

    Parameters:
        client_id (str): The ID of the client to retrieve.

    Returns:
        dict: A dictionary containing the HTTP status code and either
              the client data or an error message.
    """
    try:
        client = db_consult(
            table_name=TABLE_CLIENT, key_name="client_id", key_value=client_id
        )

        if client:
            return {"statusCode": 200, "body": client}

        return {"statusCode": 404, "body": MESSAGE_404_CLIENT_STR}

    except Exception as e:
        return {"statusCode": 500, "body": f"Error in retrieve_client: {e}"}


def retrieve_sale(sale_id: str):
    """
    Retrieves sale information from the database.

    This function queries the database to find a sale by its sale ID.
    It returns the sale data if found, or an appropriate error message
    if the sale is not found or if an error occurs during the query.

    Parameters:
        sale_id (str): The ID of the sale to retrieve.

    Returns:
        dict: A dictionary containing the HTTP status code and either
              the sale data or an error message.
    """
    try:
        sale = db_consult(table_name=TABLE_SALE, key_name="sale_id", key_value=sale_id)

        if sale:
            return {"statusCode": 200, "body": Sale(**sale).model_dump()}

        return {"statusCode": 404, "body": MESSAGE_404_SALE_STR}

    except Exception as e:
        return {"statusCode": 500, "body": f"Error in retrieve_sale: {e}"}


def update_user(user_id: str, body: dict):
    """
    Updates an existing user record in the database.

    This function updates the user data in the database by adding the user ID
    to the provided data and then performing the update operation. It returns
    an appropriate status code and message based on the success or failure
    of the operation.

    Parameters:
        user_id (str): The ID of the user to update.
        body (dict): The data to update for the user.

    Returns:
        dict: A dictionary containing the HTTP status code and a message.
    """
    try:
        user = db_consult(
            table_name=TABLE_USER, key_name="user_id", key_value=str(body["user_id"])
        )
        
        if not user:
            return {"statusCode": 404, "body": MESSAGE_404_USER_STR}
        
        body.update({"user_id": user_id})

        user_item = User(**body).model_dump()

        status = db_insert(table_name=TABLE_USER, item=user_item)

        if status != 200:
            return {"statusCode": status, "body": MESSAGE_FAIL_UPDATE_STR}

        return {"statusCode": 200, "body": f"User {user_id} updated successfully"}

    except Exception as e:
        return {"statusCode": 500, "body": f"Error in update_user: {e}"}


def update_client(client_id: str, body: dict):
    """
    Creates or updates a client record in the database.

    This function updates the client data with the provided client ID
    and then inserts or updates the record in the database. It returns
    an appropriate status code and message based on the success or failure
    of the operation.

    Parameters:
        client_id (str): The ID of the client to create or update.
        body (dict): The data for the client, including fields to be updated or created.

    Returns:
        dict: A dictionary containing the HTTP status code and a message.
    """
    try:
        client = db_consult(
            table_name=TABLE_CLIENT, key_name="client_id", key_value=client_id
        )
        
        if not client:
            return {"statusCode": 404, "body": MESSAGE_404_CLIENT_STR}
        
        body.update({"client_id": client_id})

        client_item = Client(**body)

        status = db_insert(table_name=TABLE_CLIENT, item=client_item.model_dump())

        if status != 200:
            return {"statusCode": status, "body": MESSAGE_FAIL_UPDATE_STR}

        event_bridge_put_event(
            source="business-api",
            detail_type="client_updated",
            detail=client_item.model_dump_json(),
        )

        return {"statusCode": 200, "body": f"Client {client_id} updated successfully"}

    except Exception as e:
        return {"statusCode": 500, "body": f"Error in create_client: {e}"}


def update_sale(sale_id: str, body: dict):
    """
    Updates an existing sale record in the database.

    This function updates the sale data with the provided sale ID
    and then performs the update operation in the database. It returns
    an appropriate status code and message based on the success or failure
    of the operation.

    Parameters:
        sale_id (str): The ID of the sale to update.
        body (dict): The data to update for the sale.

    Returns:
        dict: A dictionary containing the HTTP status code and a message.
    """
    try:
        sale = db_consult(table_name=TABLE_SALE, key_name="sale_id", key_value=sale_id)
        
        if not sale:
            return {"statusCode": 404, "body": MESSAGE_404_SALE_STR}
            
        body.update({"sale_id": sale_id})

        sale_item = Sale(**body).model_dump()

        status = db_insert(table_name=TABLE_SALE, item=sale_item)

        if status != 200:
            return {"statusCode": status, "body": MESSAGE_FAIL_UPDATE_STR}

        return {"statusCode": 200, "body": f"Sale {sale_id} updated successfully"}

    except Exception as e:
        return {"statusCode": 500, "body": f"Error in create_sale: {e}"}


def delete_user(user_id: str):
    """
    Deletes an existing user record from the database.

    This function deletes the user record with the provided user ID
    from the database. It returns an appropriate status code and message
    based on the success or failure of the operation.

    Parameters:
        user_id (str): The ID of the user to delete.

    Returns:
        dict: A dictionary containing the HTTP status code and a message.
    """
    try:
        user = db_consult(table_name=TABLE_USER, key_name="user_id", key_value=str(user_id))
        
        if not user:
            return {"statusCode": 404, "body": MESSAGE_404_USER_STR}
        
        status = db_delete(table_name=TABLE_USER, key_name="user_id", key_value=user_id)

        if status != 200:
            return {"statusCode": status, "body": MESSAGE_FAIL_DELETE_STR}

        return {"statusCode": 200, "body": f"User {user_id} deleted successfully"}

    except Exception as e:
        return {"statusCode": 500, "body": f"Error in delete_user: {e}"}


def delete_client(client_id: str):
    """
    Deletes an existing client record from the database.

    This function deletes the client record with the provided client ID
    from the database. It returns an appropriate status code and message
    based on the success or failure of the operation.

    Parameters:
        client_id (str): The ID of the client to delete.

    Returns:
        dict: A dictionary containing the HTTP status code and a message.
    """
    try:
        client = db_consult(
            table_name=TABLE_CLIENT, key_name="client_id", key_value=client_id
        )
        
        if not client:
            return {"statusCode": 404, "body": MESSAGE_404_CLIENT_STR}
        
        status = db_delete(
            table_name=TABLE_CLIENT, key_name="client_id", key_value=client_id
        )

        if status != 200:
            return {"statusCode": 404, "body": MESSAGE_FAIL_DELETE_STR}

        return {"statusCode": 200, "body": f"Client {client_id} deleted successfully"}

    except Exception as e:
        return {"statusCode": 500, "body": f"Error in delete_client: {e}"}


def delete_sale(sale_id: str):
    """
    Deletes an existing sale record from the database.

    This function deletes the sale record with the provided sale ID
    from the database. It returns an appropriate status code and message
    based on the success or failure of the operation.

    Parameters:
        sale_id (str): The ID of the sale to delete.

    Returns:
        dict: A dictionary containing the HTTP status code and a message.
    """
    try:
        sale = db_consult(table_name=TABLE_SALE, key_name="sale_id", key_value=sale_id)
        
        if not sale:
            return {"statusCode": 404, "body": MESSAGE_404_SALE_STR}
            
            
        status = db_delete(table_name=TABLE_SALE, key_name="sale_id", key_value=sale_id)

        if status != 200:
            return {"statusCode": 404, "body": MESSAGE_FAIL_DELETE_STR}

        return {"statusCode": 200, "body": f"Sale {sale_id} deleted successfully"}

    except Exception as e:
        return {"statusCode": 500, "body": f"Error in delete_sale: {e}"}
