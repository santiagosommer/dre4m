# From imports
from fastapi import APIRouter

# Local imports
from app.api.models.address_api_models import Address

router = APIRouter(
    prefix="/addresses",
    tags=["Addresses"]
)


@router.post("//")
def add_user_address(address: Address):
    print(f"Received address: {address}")
