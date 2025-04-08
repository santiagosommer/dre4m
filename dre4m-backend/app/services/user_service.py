# From imports
from sqlalchemy.orm import Session
from sqlalchemy.exc import NoResultFound

# Local imports
from app.db.connection import SessionLocal
from app.db.user_crud import (
    crud_create_user,
    crud_get_user,
    crud_delete_user
)
from app.db.models.user_models import User


def create_user(email: str, password: str) -> User:
    """
    Create a new user with the given email and password.

    :param email: Email of the user
    :param password: Password of the user
    :param db: Database session
    :return: User object if the user was created successfully
    :raises IntegrityError: If a user with the given email already exists.
    """
    db: Session = SessionLocal()
    if not email or not password:
        raise ValueError("Email and password are required")

    return crud_create_user(db, email, password)


def get_user(email: str) -> User:
    """
    Get a user by email.

    :param email: Email of the user
    :param db: Database session
    :return: User object if the user exists
    :raises NoResultFound: If no user is found with the given email.
    """
    db: Session = SessionLocal()
    try:
        user = crud_get_user(db, email)
        if not user:
            raise NoResultFound(f"No user found with email: {email}")
        return user
    except NoResultFound:
        raise
    finally:
        db.close()


def delete_user(email: str) -> None:
    """
    Delete a user by email.

    :param email: Email of the user to delete
    :param db: Database session
    :raises NoResultFound: If no user is found with the given email.
    """
    db: Session = SessionLocal()
    try:
        user = get_user(email)
        if not user:
            raise NoResultFound(f"No user found with email: {email}")
        return crud_delete_user(db, email)
    finally:
        db.close()
