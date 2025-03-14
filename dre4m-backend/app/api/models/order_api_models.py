# From imports
from pydantic import BaseModel


class Order(BaseModel):
    name: str
    price: int
