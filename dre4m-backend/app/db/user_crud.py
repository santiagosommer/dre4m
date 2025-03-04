# From imports
from typing import List
from .connection import SessionLocal
from .models.users_models import User
from ..logging_config import logger

# SQLAlchemy imports
from sqlalchemy import select
from sqlalchemy.orm import Session
from sqlalchemy.exc import MultipleResultsFound
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.exc import IntegrityError
from sqlalchemy.exc import NoResultFound


def create_user(email: str, password: str) -> User | None:
    """
    Create a new user with the given email and password.

    :param email: Email of the user
    :param password: Password of the user
    :return: User object if the user was created successfully, None otherwise
    """
    db: Session = SessionLocal()
    try:
        db_user: User = User(email=email, password=password)
        # Add the object to the session
        db.add(db_user)
        # Commit the session to apply the changes to the database
        db.commit()
        # Refresh the object to get the id
        db.refresh(db_user)

        logger.info(f"User with email {email} created successfully.")
        return db_user
    except IntegrityError:
        db.rollback()
        logger.error(f"User with email {email} already exists.")
        return None
    except SQLAlchemyError:
        db.rollback()
        logger.error(f"Error creating user with email {email}.")
        return None
    finally:
        db.close()


def get_user(email: str) -> User | None:
    """
    Check if a user with the given username already exists in the database.
    SQLAlchemy uses parametric queries to prevent SQL injection attacks.

    :param email: Email to check
    :return: User object if the user exists, None otherwise
    """
    db: Session = SessionLocal()
    try:
        where_user_query = select(User).where(
            User.email == email)  # type: ignore
        user_match = db.execute(where_user_query).scalar_one_or_none()

        if user_match:
            logger.info(f"User with email {email} found.")
        else:
            logger.info(f"User with email {email} not found.")
        return user_match
    except MultipleResultsFound:
        logger.error(f"Multiple users found with email {email}.")
    except SQLAlchemyError:
        logger.error(f"Error getting user with email {email}.")
    finally:
        db.close()


def list_users() -> List[User] | None:
    """
    List all users in the database.

    :return: List of User objects
    """
    db = SessionLocal()
    try:
        users = db.query(User).all()
        return users
    except SQLAlchemyError:
        logger.error("Error listing users")
    finally:
        db.close()


def update_user():
    pass


def delete_user(email: str) -> None:
    """
    Delete a user with the given email.

    :param email: Email of the user to delete
    """
    db = SessionLocal()
    try:
        user_to_delete = get_user(email)

        if not user_to_delete:
            raise NoResultFound

        db.delete(user_to_delete)
        db.commit()
        logger.info(f"User with email {email} deleted successfully.")
    except NoResultFound:
        logger.error(f"User with email {email} not found.")
    except SQLAlchemyError:
        db.rollback()
        logger.error(f"Error deleting user with email {email}.")
        raise SQLAlchemyError
    finally:
        db.close()
