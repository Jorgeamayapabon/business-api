import json
from typing import List
from pydantic import BaseModel, field_validator


class User(BaseModel):
    """
    Model representing a user record.

    This class defines the structure of a user record, including the user's unique identifier,
    full name, and email address. It also includes validation to ensure that the `user_id` is a string.

    Attributes:
        user_id (str): The unique identifier for the user.
        fullname (str): The full name of the user.
        email (str): The email address of the user.

    Methods:
        validate_user_id(value: str) -> str:
            Ensures that the `user_id` attribute is a string.
    """

    user_id: str
    fullname: str
    email: str

    @field_validator("user_id", mode="before")
    def validate_user_id(cls, value):
        return str(value)


class Client(BaseModel):
    """
    Model representing a client record.

    This class defines the structure of a client record, including the client's unique identifier,
    full name, and email address. It also includes validation to ensure that the `client_id` is a string.

    Attributes:
        client_id (str): The unique identifier for the client.
        fullname (str): The full name of the client.
        email (str): The email address of the client.

    Methods:
        validate_client_id(value: str) -> str:
            Ensures that the `client_id` attribute is a string.
    """

    client_id: str
    fullname: str
    email: str

    @field_validator("client_id", mode="before")
    def validate_client_id(cls, value):
        return str(value)


class Sale(BaseModel):
    """
    Model representing a sale record.

    This class defines the structure of a sale record, including identifiers for the sale, user, and client,
    as well as the value of the sale. It also includes validation to ensure that the `value` is an integer
    and identifiers are strings.

    Attributes:
        sale_id (str): The unique identifier for the sale.
        user_id (str): The identifier for the user associated with the sale.
        client_id (str): The identifier for the client associated with the sale.
        value (int): The value of the sale.

    Methods:
        validate_value(value: int) -> int:
            Ensures that the `value` attribute is an integer.

        validate_sale_id(value: str) -> str:
            Ensures that the `sale_id` attribute is a string.

        validate_user_id(value: str) -> str:
            Ensures that the `user_id` attribute is a string.

        validate_client_id(value: str) -> str:
            Ensures that the `client_id` attribute is a string.
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


class BodyRecord(BaseModel):
    """
    Model representing the body of a record in an event.

    This class defines the structure of the `body` attribute in a record. It includes details about
    a `User`, `Client`, and `Sale`. Each attribute is an instance of the respective model class.

    Attributes:
        user (User): An instance of the `User` model representing the user associated with the record.
        client (Client): An instance of the `Client` model representing the client associated with the record.
        sale (Sale): An instance of the `Sale` model representing the sale associated with the record.
    """

    user: User
    client: Client
    sale: Sale


class RecordEvent(BaseModel):
    """
    Model representing an individual record within an event.

    This class defines the structure of a single record in an event, specifically focusing on the
    `body` attribute which is an instance of `BodyRecord`. The `body` attribute is validated to
    ensure it is either a dictionary or can be converted from a JSON string.

    Attributes:
        body (BodyRecord): The content of the record, represented as an instance of `BodyRecord`.

    Methods:
        validate_body(value: Any) -> BodyRecord:
            Ensures that the `body` attribute is a dictionary. If the input is a JSON string, it
            converts it to a dictionary before validation.
    """

    body: BodyRecord

    @field_validator("body", mode="before")
    def validate_body(cls, value):
        if not isinstance(value, dict):
            return json.loads(value)
        return value


class RecordsEvent(BaseModel):
    """
    Model representing an event with a list of records.

    This class defines the structure of an event that contains a list of records. Each record is
    represented by an instance of the `RecordEvent` class.

    Attributes:
        Records (List[RecordEvent]): A list of `RecordEvent` objects, representing individual records in the event.
    """

    Records: List[RecordEvent]
