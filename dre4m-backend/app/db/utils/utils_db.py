# Imports
import os

# From imports
from dotenv import load_dotenv
from .init_queries import CREATE_USERS_TABLE_QUERY
from ..connection import SessionLocal
from ...exceptions import InitDatabaseError
from ...logging_config import logger

# SQKAlchemy imports
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.sql import text

# Remove after developing the app
load_dotenv()

DB_USER_QUERY = os.getenv(
    "CREATE_DB_USERS_QUERY"
)


def create_db_user():
    """
    Creates the database user 'dream_admin' if it does not exist.
    It logs the result of the operation.
    """
    try:
        # Create the new database user
        db = SessionLocal()

        if DB_USER_QUERY is None:
            raise InitDatabaseError(
                "DB_USER_QUERY environment variable is not set")

        db.execute(text(DB_USER_QUERY))
        db.commit()
        db.close()
        logger.info("Database admin user created successfully.")
    except SQLAlchemyError:
        logger.error("Error creating database user 'dream_admin'")
        raise InitDatabaseError("Error creating database user")


def create_table():
    """
    Creates the table 'users' if it does not exist.
    It logs the result of the operation.
    """
    try:
        # Create the new database user
        db = SessionLocal()
        db.execute(CREATE_USERS_TABLE_QUERY)
        db.commit()
        db.close()
        logger.info("Users table created successfully)")
    except SQLAlchemyError:
        logger.error("Error creating table 'users'")
        raise InitDatabaseError("Error creating database user")
