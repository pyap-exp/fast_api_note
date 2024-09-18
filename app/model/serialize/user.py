from pydantic import BaseModel


class UserAccess(BaseModel):
    name:str

class GetUserAuth(BaseModel):
    token:str
