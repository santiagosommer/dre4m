# From imports
from pydantic import BaseModel, EmailStr
from app.api.models.address_api_models import Address


# Object definition for users
class User(BaseModel):
    email: EmailStr
    password: str


class Admin(User):
    role: str


class Customer(User):
    name: str
    lastname: str
    billing_address: Address
    shipping_address: Address
