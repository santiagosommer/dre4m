# From imports
from pydantic import BaseModel


class Product(BaseModel):
    name: str
    description: str
    price: float
    stock: int
    product_img: str
