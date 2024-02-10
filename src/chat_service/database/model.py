"""
Schema Models
"""

import datetime
from pydantic import BaseModel

class User(BaseModel):
    '''Represents User class'''
    username: str
    email: str
    first_name: str
    last_name: str
    is_active: bool

class Thread(BaseModel):
    '''Represents Thread class'''
    name: str
    date_created: datetime.time

class Message(BaseModel):
    '''Represents Message class'''
    message: str
    date_created: datetime.time
    role: str


class UserThreadMessage(BaseModel):
    '''Represents Thread Message Link'''
    user_id: int
    message_id: int
    thrad_id: int