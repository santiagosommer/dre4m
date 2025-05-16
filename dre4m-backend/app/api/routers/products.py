# From imports
from fastapi import APIRouter
from fastapi.responses import JSONResponse

# Local imports
from app.api.models.product_api_models import Product

router = APIRouter(
    prefix="/products",
    tags=["Products"]
)


@router.post("/")
async def create_product_endpoint(product: Product):
    print(product)


@router.get("/list")
async def list_products():
    returning_products = [
        {
            "id": "1",
            "name": "ART 001 TSHIRT",
            "price": "999",
            "img": "idk"
        },
        {
            "id": "2",
            "name": "ART 002 TSHIRT",
            "price": "999",
            "img": "idk"
        },
        {
            "id": "3",
            "name": "ART 003 TSHIRT",
            "price": "999",
            "img": "idk"
        }
    ]
    return JSONResponse(content=returning_products)
