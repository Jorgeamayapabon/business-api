import json
from typing import List
from pydantic import BaseModel, field_validator


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


class BodyRecord(BaseModel):
    user: User
    client: Client
    sale: Sale


class RecordEvent(BaseModel):
    body: BodyRecord
    
    @field_validator("body", mode="before")
    def validate_body(cls, value):
        if not isinstance(value, dict):
            return json.loads(value)
        return value

class RecordsEvent(BaseModel):
    Records: List[RecordEvent]
