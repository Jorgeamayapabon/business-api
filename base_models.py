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
    user_id: str | int
    fullname: str
    email: str
    
    def __init__(self, **data):
        super().__init__(**data)
        self.user_id = self._cast_str()
    
    def _cast_str(self):
        if not isinstance(self.user_id, str):
            return str(self.user_id)

        return self.user_id


class Client(BaseModel):
    client_id: str | int
    name: str
    email: str
    
    def __init__(self, **data):
        super().__init__(**data)
        self.client_id = self._cast_str()
    
    def _cast_str(self):
        if not isinstance(self.client_id, str):
            return str(self.client_id)

        return self.client_id


class Sale(BaseModel):
    sale_id: str | int
    user_id: str
    client_id: str
    value: float

    def __init__(self, **data):
        super().__init__(**data)
        self.sale_id = self._cast_str()
    
    def _cast_str(self):
        if not isinstance(self.sale_id, str):
            return str(self.sale_id)

        return self.sale_id
