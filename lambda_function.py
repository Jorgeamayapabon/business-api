from base_models import HttpRequest, HttpResponse
from http_methods import http_create, http_delete, http_retreive, http_update


def lambda_handler(event, context):
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
