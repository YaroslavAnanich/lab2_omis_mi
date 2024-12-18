from pydantic import BaseModel
from datetime import date

class UserLoginSchem(BaseModel):
    email: str
    password: str


class UserRegisterSchem(UserLoginSchem):
    name: str
    phone: str


class TableSchem(BaseModel):
    location: str
    service: str
    price: int


class BookSchem(BaseModel):
    table_date: date
    notification_id: int


class NotificationSchem(BaseModel):
    text: str
    degree_of_importance: str
    notification_date: date
    user_id: int
    table_id: int






