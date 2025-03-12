# Imports
import os
import psycopg2

# From imports
from sqlalchemy import create_engine
from dotenv import load_dotenv
from app.exceptions import MissingEnvironmentVariableError
from app.logging_config import logger
from app.db.models.users_models import Base

"""
This module contains utility functions for creating the database and tables.

Important: If changing the way to get the data from environment variables,
parametrize the queries in the functions to avoid SQL injection attacks.
"""

# Remove after developing the app
load_dotenv()

# Missing password in the connection string
DEFAULT_DB_USER = os.getenv("DEFAULT_DB_USER")
DB_NEW_USER = os.getenv("DB_USER")
DB_NEW_USER_PASSWORD = os.getenv("DB_USER_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

if not all([DEFAULT_DB_USER, DB_NEW_USER,
            DB_NEW_USER_PASSWORD, DB_HOST,
            DB_PORT, DB_NAME]):
    raise MissingEnvironmentVariableError("Missing environment variables")


def create_db():
    """
    Creates the database if it does not exist.
    """
    try:
        conn = psycopg2.connect(
            dbname="postgres",
            user=DEFAULT_DB_USER,
            host=DB_HOST,
            port=DB_PORT
        )
        conn.autocommit = True
        cur = conn.cursor()

        # Check if the database exists
        cur.execute(
            "SELECT 1 FROM pg_database WHERE datname = %s;", (DB_NAME,)
        )
        exists = cur.fetchone()

        if not exists:
            cur.execute(
                f"CREATE DATABASE {DB_NAME};"
            )
            logger.info(f"Database {DB_NAME} created.")
        else:
            logger.info(f"Database {DB_NAME} already exists.")

        cur.close()
        conn.close()

    except Exception as e:
        logger.error(f"Error creating database: {e}")


def create_db_user():
    """
    Creates a database user if it does not exist.
    Ensure that create database function is called before this function.
    """
    conn = psycopg2.connect(
        dbname=DB_NAME,
        user=DEFAULT_DB_USER,
        host=DB_HOST,
        port=DB_PORT
    )
    conn.autocommit = True
    cur = conn.cursor()

    # Check if the user already exists
    cur.execute(
        f"SELECT 1 FROM pg_roles WHERE rolname='{DB_NEW_USER}';"
    )
    exists = cur.fetchone()

    if not exists:
        cur.execute(
            f"CREATE USER {DB_NEW_USER} WITH "
            f"PASSWORD '{DB_NEW_USER_PASSWORD}' "
            f"CREATEDB CREATEROLE REPLICATION BYPASSRLS LOGIN;"
        )
        logger.info(f"User {DB_NEW_USER} created.")
    else:
        logger.info(f"User {DB_NEW_USER} already exists.")

    cur.close()
    conn.close()


def create_tables():
    """
    Creates the tables defined in the SQLAlchemy models.
    """
    DATABASE_URL = (
        f"postgresql://{DEFAULT_DB_USER}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    )
    engine = create_engine(DATABASE_URL, echo=False)
    Base.metadata.create_all(bind=engine)
    print(f'Created tables: {list(Base.metadata.tables.keys())}')
