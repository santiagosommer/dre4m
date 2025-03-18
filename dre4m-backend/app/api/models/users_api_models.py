# From imports
from pydantic import BaseModel, EmailStr
from typing import List
from app.api.models.address_api_models import Address
from app.api.models.order_api_models import Order


# Object definition for users
class User(BaseModel):
    email: EmailStr
    password: str


class Admin(User):
    pass


class Customer(User):
    name: str
    lastname: str
    billing_address: Address
    shipping_address: Address
    orders: List[Order]
