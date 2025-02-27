from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, declarative_base
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env

# URL de conexión a PostgreSQL
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://user:password@localhost:5432/dre4mdb")

DATABASE_USER = "example_user"
DATABASE_USER_PASSWORD = "1234"

# Crear el motor de la base de datos
engine = create_engine(DATABASE_URL)

# Crear una sesión
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para los modelos
Base = declarative_base()

# Function to create a user
def create_user():
    with engine.connect() as connection:
        # Check if the user already exists
        result = connection.execute(text(f"SELECT 1 FROM pg_roles WHERE rolname = :username"), {'username': DATABASE_USER})
        if result.fetchone():
            print(f"User '{DATABASE_USER}' already exists.")
        else:
            # Create the user
            connection.execute(text(f"CREATE USER {DATABASE_USER} WITH PASSWORD :database_password"), {'database_password': DATABASE_USER_PASSWORD})
            print(f"User '{DATABASE_USER}' created successfully.")

# Call the function to create the user
create_user()