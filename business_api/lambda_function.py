from base_models import HttpRequest, HttpResponse
from http_methods import http_create, http_delete, http_retreive, http_update


def lambda_handler(event, context):
    """
    AWS Lambda function handler for processing HTTP requests.

    This function handles incoming events based on their HTTP method (POST, GET, PUT, DELETE).
    It parses the event into an `HttpRequest` object and delegates the request to the appropriate
    function (`http_create`, `http_retreive`, `http_update`, or `http_delete`). If the HTTP method
    is not one of the supported methods, it returns a 405 Method Not Allowed response.

    Parameters:
        event (dict): The event data passed to the Lambda function, which should include HTTP method,
                      path, and optionally a body.
        context (object): The context object provides runtime information (e.g., function name, version).

    Returns:
        dict: The response from the delegated function or a 405 Method Not Allowed response if the method
              is unsupported. The response is formatted as an `HttpResponse` object.

    Raises:
        ValueError: If `event` does not have the required keys or if the HTTP method is unsupported.
    """
    print(event)

    http_request = HttpRequest(**event)

    if http_request.httpMethod in ["POST", "GET", "PUT", "DELETE"]:
        if http_request.httpMethod == "POST":
            return http_create(path=http_request.path, body=http_request.body)

        elif http_request.httpMethod == "GET":
            return http_retreive(path=http_request.path)

        elif http_request.httpMethod == "PUT":
            return http_update(path=http_request.path, body=http_request.body)

        elif http_request.httpMethod == "DELETE":
            return http_delete(path=http_request.path)

    return HttpResponse(statusCode=405, body="Method not allowed").model_dump()
