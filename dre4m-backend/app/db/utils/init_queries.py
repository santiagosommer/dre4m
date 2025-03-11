# From imports
from sqlalchemy.sql import text


# SQL queries for initializing the database

# Create the users table
CREATE_USERS_TABLE_QUERY = text("""
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    email VARCHAR(50) NOT NULL,
    password VARCHAR(50) NOT NULL
)
""")
