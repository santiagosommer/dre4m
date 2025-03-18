# From imports
from pydantic import BaseModel
from typing import List
from app.api.models.product_api_models import Product


class Order(BaseModel):
    name: str
    total: int
    state: str
    product_list: List[Product]
    created_at: int  # type Datetime
