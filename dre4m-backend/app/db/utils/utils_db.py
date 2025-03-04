# From imports
from ...exceptions import InitDatabaseError
from ..connection import SessionLocal
from sqlalchemy.exc import SQLAlchemyError
from .sql_queries import CREATE_USERS_TABLE_QUERY
from .sql_queries import CREATE_DB_USERS
from ...logging_config import logger


def create_db_user():
    try:
        # Create the new database user
        db = SessionLocal()
        db.execute(CREATE_DB_USERS)
        db.commit()
        db.close()
        logger.info("Database user 'dream_admin' created successfully.")
    except SQLAlchemyError:
        logger.error("Error creating database user 'dream_admin'")
        raise InitDatabaseError("Error creating database user")


def create_table():
    try:
        # Create the new database user
        db = SessionLocal()
        db.execute(CREATE_USERS_TABLE_QUERY)
        db.commit()
        db.close()
        logger.info("Table 'users' created successfully)")
    except SQLAlchemyError:
        logger.error("Error creating table 'users'")
        raise InitDatabaseError("Error creating database user")
