import json
from pydantic import BaseModel, field_validator

class HttpRequest(BaseModel):
    """
    Represents an HTTP request.

    This class models the structure of an HTTP request, including the 
    HTTP method, path, and optional body. It includes validation to ensure
    the body is a dictionary, deserializing it from a JSON string if necessary.

    Attributes:
        httpMethod (str): The HTTP method of the request (e.g., 'GET', 'POST').
        path (str): The URL path of the request.
        body (dict | None): The body of the request, if any.

    Methods:
        validate_body(cls, value): Validates and deserializes the body if needed.

    Examples:
        >>> HttpRequest(httpMethod='POST', path='/users', body='{"name": "John"}')
        HttpRequest(httpMethod='POST', path='/users', body={'name': 'John'})
        
        >>> HttpRequest(httpMethod='GET', path='/users', body=None)
        HttpRequest(httpMethod='GET', path='/users', body=None)
    """
    httpMethod: str
    path: str
    body: dict | None
    
    @field_validator("body", mode="before")
    def validate_body(cls, value):
        if value and not isinstance(value, dict):
            return json.loads(value)

        return value


class HttpResponse(BaseModel):
    """
    Represents an HTTP response.

    This class models the structure of an HTTP response, including the 
    status code and body. It includes validation to ensure the body is a
    JSON string, serializing it if necessary.

    Attributes:
        statusCode (int): The HTTP status code of the response.
        body (str): The body of the response, serialized as a JSON string.

    Methods:
        validate_body(cls, value): Validates and serializes the body if needed.

    Examples:
        >>> HttpResponse(statusCode=200, body={"message": "Success"})
        HttpResponse(statusCode=200, body='{"message": "Success"}')
        
        >>> HttpResponse(statusCode=404, body="Not Found")
        HttpResponse(statusCode=404, body='{"message": "Not Found"}')
    """
    statusCode: int
    body: str

    @field_validator("body", mode="before")
    def validate_body(cls, value):
        if not isinstance(value, str):
            return json.dumps(value)
        
        return json.dumps({"message": value})


class User(BaseModel):
    """
    Represents a user in the system.

    This class models the structure of a user, including the user ID, full name, and email address.
    It includes validation to ensure the user ID is a string.

    Attributes:
        user_id (str): The unique identifier for the user.
        fullname (str): The full name of the user.
        email (str): The email address of the user.

    Methods:
        validate_user_id(cls, value): Ensures the user ID is a string.

    Examples:
        >>> User(user_id=123, fullname="John Doe", email="john.doe@example.com")
        User(user_id='123', fullname='John Doe', email='john.doe@example.com')
        
        >>> User(user_id="456", fullname="Jane Smith", email="jane.smith@example.com")
        User(user_id='456', fullname='Jane Smith', email='jane.smith@example.com')
    """
    user_id: str
    fullname: str
    email: str
    
    @field_validator("user_id", mode="before")
    def validate_user_id(cls, value):
        return str(value)


class Client(BaseModel):
    """
    Represents a client in the system.

    This class models the structure of a client, including the client ID, full name, and email address.
    It includes validation to ensure the client ID is a string.

    Attributes:
        client_id (str): The unique identifier for the client.
        fullname (str): The full name of the client.
        email (str): The email address of the client.

    Methods:
        validate_client_id(cls, value): Ensures the client ID is a string.

    Examples:
        >>> Client(client_id=123, fullname="Acme Corp", email="contact@acme.com")
        Client(client_id='123', fullname='Acme Corp', email='contact@acme.com')
        
        >>> Client(client_id="456", fullname="Tech Innovations", email="info@techinnovations.com")
        Client(client_id='456', fullname='Tech Innovations', email='info@techinnovations.com')
    """
    client_id: str
    fullname: str
    email: str
    
    @field_validator("client_id", mode="before")
    def validate_client_id(cls, value):
        return str(value)


class Sale(BaseModel):
    """
    Represents a sale record in the system.

    This class models the structure of a sale, including the sale ID, user ID, client ID, and the sale value.
    It includes validation to ensure all IDs are strings and the value is an integer.

    Attributes:
        sale_id (str): The unique identifier for the sale.
        user_id (str): The unique identifier for the user associated with the sale.
        client_id (str): The unique identifier for the client associated with the sale.
        value (int): The value of the sale.

    Methods:
        validate_value(cls, value): Ensures the sale value is an integer.
        validate_sale_id(cls, value): Ensures the sale ID is a string.
        validate_user_id(cls, value): Ensures the user ID is a string.
        validate_client_id(cls, value): Ensures the client ID is a string.

    Examples:
        >>> Sale(sale_id=123, user_id="456", client_id="789", value=100)
        Sale(sale_id='123', user_id='456', client_id='789', value=100)
        
        >>> Sale(sale_id="124", user_id="457", client_id="790", value="150")
        Sale(sale_id='124', user_id='457', client_id='790', value=150)
    """
    sale_id: str
    user_id: str
    client_id: str
    value: int
    
    @field_validator("value", mode="before")
    def validate_value(cls, value):
        return int(value)
    
    @field_validator("sale_id", mode="before")
    def validate_sale_id(cls, value):
        return str(value)
    
    @field_validator("user_id", mode="before")
    def validate_user_id(cls, value):
        return str(value)
    
    @field_validator("client_id", mode="before")
    def validate_client_id(cls, value):
        return str(value)
