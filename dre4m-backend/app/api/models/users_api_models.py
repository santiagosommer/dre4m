# From imports
from pydantic import BaseModel, EmailStr
from typing import List, Optional

# Local imports
from app.api.models.address_api_models import Address
from app.api.models.order_api_models import Order


# Object definition for users
class ApiUser(BaseModel):
    email: EmailStr
    password: str


class Admin(ApiUser):
    pass


class Customer(ApiUser):
    name: str
    lastname: str
    billing_address: Optional[Address]
    shipping_address: Optional[Address]
    orders: List[Order] = []
