from datetime import datetime
from pydantic import BaseModel
from typing import Optional


class BaseModelModify(BaseModel):
    id: Optional[int] = None

class Users(BaseModelModify):
    login: str
    password : str
    power_level: Optional[int]

class Service(BaseModelModify):
    name: Optional[str]
    
class Applications(BaseModelModify):
    add_date: str
    UserID: int
    serviceID: int
    comments: Optional[str]
    date_completion: Optional[str]
