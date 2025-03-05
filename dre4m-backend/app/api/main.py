# From imports
from typing import Union
from fastapi import FastAPI
from dotenv import load_dotenv

# Loads environment variables from .env file
load_dotenv()

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(
    item_id: int,
    q: Union[str, None] = None
) -> dict[str, Union[int, Union[str, None]]]:
    return {"item_id": item_id, "q": q}
