# From imports
from ..auth.hashing import hash_password
# SQLAlchemy imports
from sqlalchemy.orm import Session
from sqlalchemy.exc import NoResultFound

# Local imports
from app.db.connection import SessionLocal
from app.db.user_crud import (
    crud_create_user,
    crud_get_user,
    crud_delete_user
)
from ..api.models.users_api_models import ApiUser
from ..exceptions import UserAlreadyExistsError


def create_user(email: str, password: str) -> ApiUser:
    """
    Create a new user with the given email and password.

    :param email: Email of the user
    :param password: Password of the user
    :param db: Database session
    :return: ApiUser object if the user was created successfully
    :raises IntegrityError: If a user with the given email already exists.
    """
    try:
        if not email or not password:
            raise ValueError("Email and password are required")

        # Verify existance
        if get_user(email):
            raise UserAlreadyExistsError(
                f"User with email {email} already exists.")

        # Hash the password
        hashed_password = hash_password(password)

        db: Session = SessionLocal()
        created_user = crud_create_user(db, email, hashed_password)
        db.close()

        return created_user
    except UserAlreadyExistsError:
        raise


def get_user(email: str) -> ApiUser | None:
    """
    Get a user by email.

    :param email: Email of the user
    :param db: Database session
    :return: ApiUser object if the user exists, None otherwise
    :raises NoResultFound: If no user is found with the given email.
    """
    db: Session = SessionLocal()
    api_user = None

    db_user = crud_get_user(db, email)

    if db_user:
        api_user = ApiUser(email=str(db_user.email),
                           password=str(db_user.password))

    db.close()

    return api_user


def delete_user(email: str) -> None:
    """
    Delete a user by email.

    :param email: Email of the user to delete
    :param db: Database session
    :raises NoResultFound: If no user is found with the given email.
    """
    db: Session = SessionLocal()
    try:
        db_user = get_user(email)
        if not db_user:
            raise NoResultFound(f"No user found with email: {email}")
        return crud_delete_user(db, email)
    finally:
        db.close()


def login_user():
    # need to recheck hash function to update
    pass
