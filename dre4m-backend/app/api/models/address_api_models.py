# From imports
from pydantic import BaseModel


class Address(BaseModel):
    street_address: str
    address_info: str
    city: str
    state_or_province: str
    zip_code: str
    country: str
    phone_number: str
