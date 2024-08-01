import re
from base_models import HttpResponse
from constants import (
    MESSAGE_404_STR,
    PATTERN_CLIENT_ID_R_STR,
    PATTERN_CLIENTS_R_STR,
    PATTERN_SALE_ID_R_STR,
    PATTERN_SALES_R_STR,
    PATTERN_USERS_ID_R_STR,
    PATTERN_USERS_R_STR,
)
from query_template import (
    create_client,
    create_sale,
    create_user,
    delete_client,
    delete_sale,
    delete_user,
    retrieve_client,
    retrieve_sale,
    retrieve_user,
    update_client,
    update_sale,
    update_user,
)


def http_create(path: str, body: dict):
    """
    Handles HTTP POST requests to create new records in the database.

    This function matches the provided path against predefined patterns to
    create new user, client, or sale records. If no pattern is matched,
    it returns a 404 Not Found response. In case of an error, it returns
    a 500 Internal Server Error response with an error message.

    Parameters:
        path (str): The URL path of the HTTP request.
        body (dict): The body of the HTTP request containing the data for the new record.

    Returns:
        dict: A dictionary representing the HTTP response.

    Raises:
        Exception: If an error occurs during the request handling.
    """
    try:
        if re.match(PATTERN_USERS_R_STR, path):
            return HttpResponse(**create_user(body=body).model_dump())

        elif re.match(PATTERN_CLIENTS_R_STR, path):
            return HttpResponse(**create_client(body=body).model_dump())

        elif re.match(PATTERN_SALES_R_STR, path):
            return HttpResponse(**create_sale(body=body).model_dump())

        else:
            return HttpResponse(statusCode=404, body=MESSAGE_404_STR).model_dump()

    except Exception as e:
        response = HttpResponse(
            statusCode=500, body=f"Error in http_create: {e}"
        ).model_dump()
        print(response)
        return response


def http_retreive(path: str):
    """
    Handles HTTP requests and returns responses based on URL patterns.

    This function matches the provided path against predefined patterns to
    retrieve user, client, or sale information. If no pattern is matched,
    it returns a 404 Not Found response. In case of an error, it returns
    a 500 Internal Server Error response with an error message.

    Parameters:
        path (str): The URL path of the HTTP request.

    Returns:
        dict: A dictionary representing the HTTP response.

    Raises:
        Exception: If an error occurs during the request handling.
    """
    try:
        path_split = path.split("/")

        if re.match(PATTERN_USERS_ID_R_STR, path):
            return HttpResponse(**retrieve_user(user_id=path_split[-1])).model_dump()

        elif re.match(PATTERN_CLIENT_ID_R_STR, path):
            return HttpResponse(
                **retrieve_client(client_id=path_split[-1])
            ).model_dump()

        elif re.match(PATTERN_SALE_ID_R_STR, path):
            return HttpResponse(**retrieve_sale(sale_id=path_split[-1])).model_dump()

        else:
            return HttpResponse(statusCode=404, body=MESSAGE_404_STR).model_dump()

    except Exception as e:
        response = HttpResponse(
            statusCode=500, body=f"Error in http_retreive: {e}"
        ).model_dump()
        print(response)
        return response


def http_update(path: str, body: dict):
    """
    Handles HTTP PUT requests to update existing records in the database.

    This function matches the provided path against predefined patterns to
    update user, client, or sale records. If no pattern is matched,
    it returns a 404 Not Found response. In case of an error, it returns
    a 500 Internal Server Error response with an error message.

    Parameters:
        path (str): The URL path of the HTTP request.
        body (dict): The body of the HTTP request containing the data for the update.

    Returns:
        dict: A dictionary representing the HTTP response.

    Raises:
        Exception: If an error occurs during the request handling.
    """
    try:
        path_split = path.split("/")

        if re.match(PATTERN_USERS_ID_R_STR, path):
            return HttpResponse(
                **update_user(user_id=path_split[-1], body=body).model_dump()
            )

        elif re.match(PATTERN_CLIENT_ID_R_STR, path):
            return HttpResponse(
                **update_client(client_id=path_split[-1], body=body).model_dump()
            )

        elif re.match(PATTERN_SALE_ID_R_STR, path):
            return HttpResponse(
                **update_sale(sale_id=path_split[-1], body=body).model_dump()
            )

        else:
            return HttpResponse(statusCode=404, body=MESSAGE_404_STR).model_dump()

    except Exception as e:
        response = HttpResponse(
            statusCode=500, body=f"Error in http_update: {e}"
        ).model_dump()
        print(response)
        return response


def http_delete(path: str):
    """
    Handles HTTP DELETE requests to delete existing records from the database.

    This function matches the provided path against predefined patterns to
    delete user, client, or sale records. If no pattern is matched,
    it returns a 404 Not Found response. In case of an error, it returns
    a 500 Internal Server Error response with an error message.

    Parameters:
        path (str): The URL path of the HTTP request.

    Returns:
        dict: A dictionary representing the HTTP response.

    Raises:
        Exception: If an error occurs during the request handling.
    """
    try:
        path_split = path.split("/")

        if re.match(PATTERN_USERS_ID_R_STR, path):
            return HttpResponse(**delete_user(user_id=path_split[-1])).model_dump()

        elif re.match(PATTERN_CLIENT_ID_R_STR, path):
            return HttpResponse(**delete_client(client_id=path_split[-1])).model_dump()

        elif re.match(PATTERN_SALE_ID_R_STR, path):
            return HttpResponse(**delete_sale(sale_id=path_split[-1])).model_dump()

        else:
            return HttpResponse(statusCode=404, body=MESSAGE_404_STR).model_dump()

    except Exception as e:
        response = HttpResponse(
            statusCode=500, body=f"Error in http_retreive: {e}"
        ).model_dump()
        print(response)
        return response
