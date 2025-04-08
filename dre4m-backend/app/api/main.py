from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from app.api.models.users_api_models import User

# Local imports
from app.api.models.users_api_models import User
from app.api.models.address_api_models import Address
from app.api.models.product_api_models import Product
from app.api.models.order_api_models import Order
from app.services.user_service import create_user

# Loads environment variables from .env file
load_dotenv()

app = FastAPI()

# CORS configuration
origins = [
    "http://localhost:5173",
    "http://127.0.0.1:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# CORS configuration
origins = [
    "http://localhost:5173",
    "http://127.0.0.1:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/product")
def list_products():
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
    return returning_products


@app.post("/addresses/")
def add_user_address(address: Address):
    print(f"Received address: {address}")


@app.post("/users/")
def create_user_endpoint(user: User):
    print(user.email, user.password)
    try:
        create_user(user.email, user.password)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    return {"user": user}


@app.post("/products/")
def create_product_endpoint(product: Product):
    print(product)


@app.post("/orders/")
def create_order_endpoint(order: Order):
    print(order)
