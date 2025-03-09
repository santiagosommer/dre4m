# From imports
from fastapi import FastAPI
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware
from .models.users_api_models import User

# Loads environment variables from .env file
load_dotenv()

app = FastAPI()

# Configuración de CORS
origins = [
    "http://localhost:5173",  # Reemplaza con el origen de tu frontend
    "http://127.0.0.1:8000",  # Reemplaza con el origen de tu frontend
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


@app.post("/users/")
def create_user(user: User):
    print(user.email, user.password)
    return {"user": user}
