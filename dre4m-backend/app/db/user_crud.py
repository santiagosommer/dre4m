# From imports
from typing import List

# Local imports
from app.db.models.user_models import User
from app.logging_config import logger

# SQLAlchemy imports
from sqlalchemy import select
from sqlalchemy.orm import Session
from sqlalchemy.exc import (
    MultipleResultsFound,
    SQLAlchemyError,
    IntegrityError,
    NoResultFound
)


def crud_create_user(db: Session, email: str, password: str) -> User | None:
    """
    Create a new user with the given email and password.

    :param email: Email of the user
    :param password: Password of the user
    :return: User object if the user was created successfully, None otherwise
    :raises IntegrityError: If a user with the given email already exists.
    :raises SQLAlchemyError: If there was an error creating the user.
    """
    try:
        if crud_get_user(db, email):
            raise IntegrityError("User with this email already exists.",
                                 params={"email": email},
                                 orig=Exception("IntegrityError"))

        db_user: User = User(email=email, password=password)
        db.add(db_user)
        db.commit()
        # Refresh the object to update the id
        db.refresh(db_user)

        logger.info(f"User with email {email} created successfully.")
        return db_user
    except IntegrityError:
        db.rollback()
        logger.error(f"User with email {email} already exists.")
        raise
    except SQLAlchemyError:
        db.rollback()
        logger.error(f"Error creating user with email {email}.")
        raise


def crud_get_user(db: Session, email: str) -> User | None:
    """
    Check if a user with the given email already exists in the database.
    SQLAlchemy uses parametric queries to prevent SQL injection attacks.

    :param email: Email to check
    :return: User object if the user exists, None otherwise
    :raises MultipleResultsFound: If multiple users are found with the given 
    email.
    :raises SQLAlchemyError: If there was an error getting the user.
    """
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
        raise
    except SQLAlchemyError:
        logger.error(f"Error getting user with email {email}.")
        raise


def crud_list_users(db: Session) -> List[User] | None:
    """
    List all users in the database.

    :return: List of User objects
    :raises SQLAlchemyError: If there was an error listing the users.
    """
    try:
        users = db.query(User).all()
        return users
    except SQLAlchemyError:
        logger.error("Error listing users")
        raise


def crud_update_user():
    pass


def crud_delete_user(db: Session, email: str) -> None:
    """
    Delete a user with the given email.

    :param email: Email of the user to delete
    :raises NoResultFound: If no user is found with the given email.
    :raises SQLAlchemyError: If there was an error deleting the user.
    """
    try:
        user_to_delete = crud_get_user(db, email)

        if not user_to_delete:
            raise NoResultFound

        db.delete(user_to_delete)
        db.commit()
        logger.info(f"User with email {email} deleted successfully.")
    except NoResultFound:
        logger.error(f"User with email {email} not found.")
        raise
    except SQLAlchemyError:
        db.rollback()
        logger.error(f"Error deleting user with email {email}.")
        raise SQLAlchemyError
