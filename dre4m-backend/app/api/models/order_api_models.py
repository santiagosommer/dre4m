# From imports
from pydantic import BaseModel
from typing import List
from datetime import datetime

# Local imports
from app.api.models.product_api_models import Product
from app.api.models.address_api_models import Address
from app.enums import PaymentMethod


class Order(BaseModel):
    name: str
    total: float
    state: str
    product_list: List[Product]
    shipping_address: Address
    payment_method: PaymentMethod
    created_at: datetime
