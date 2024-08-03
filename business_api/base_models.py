import json
from pydantic import BaseModel, field_validator

class HttpRequest(BaseModel):
    httpMethod: str
    path: str
    body: dict | None
    
    @field_validator("body", mode="before")
    def validate_body(cls, value):
        if value and not isinstance(value, dict):
            return json.loads(value)

        return value


class HttpResponse(BaseModel):
    statusCode: int
    body: str

    @field_validator("body", mode="before")
    def validate_body(cls, value):
        if not isinstance(value, str):
            return json.dumps(value)
        
        return json.dumps({"message": value})


class User(BaseModel):
    user_id: str
    fullname: str
    email: str
    
    @field_validator("user_id", mode="before")
    def validate_user_id(cls, value):
        return str(value)


class Client(BaseModel):
    client_id: str
    fullname: str
    email: str
    
    @field_validator("client_id", mode="before")
    def validate_client_id(cls, value):
        return str(value)


class Sale(BaseModel):
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
