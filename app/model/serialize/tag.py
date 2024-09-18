from typing import List

from pydantic import BaseModel


class Tags(BaseModel):
    id: int
    name:str

class GetAllTags(BaseModel):
    data:List[Tags]
