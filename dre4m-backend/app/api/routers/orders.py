# From imports
from fastapi import APIRouter

# Local imports
from app.api.models.order_api_models import Order

router = APIRouter(
    prefix="/orders",
    tags=["Orders"]
)


@router.post("/")
def create_order(order: Order):
    print(f'Received: {order}')
