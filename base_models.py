import json
from pydantic import BaseModel

class HttpRequest(BaseModel):
    httpMethod: str
    path: str
    body: str | None
    
    def __init__(self, **data):
        super().__init__(**data)
        self.body = self._cast_dict()
    
    def _cast_dict(self):
        if self.body is not None:
            return json.loads(self.body)


class HttpResponse(BaseModel):
    statusCode: int
    body: str | dict

    def __init__(self, **data):
        super().__init__(**data)
        self.body = self._cast_str()
    
    def _cast_str(self):
        if isinstance(self.body, str):
            return json.dumps({"message": self.body})

        return json.dumps(self.body)


class User(BaseModel):
    user_id: str
    fullname: str
    email: str


class Client(BaseModel):
    client_id: str
    name: str
    email: str


class Sale(BaseModel):
    sale_id: str
    user_id: str
    client_id: str
    value: float
