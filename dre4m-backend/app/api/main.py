# From imports
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Local imports
from .routers import (
    users,
    addresses,
    orders,
    products
)
from app.auth import auth_router


app = FastAPI()

# CORS configuration
origins = [
    "https://localhost:5173",
    "https://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users.router)
app.include_router(addresses.router)
app.include_router(products.router)
app.include_router(orders.router)
app.include_router(auth_router.router)


@app.get("/")
async def root():
    return {"Hello": "World"}
