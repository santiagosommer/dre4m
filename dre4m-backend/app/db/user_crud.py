# From imports
from sqlalchemy.orm import Session
from sqlalchemy import select
from .connection import SessionLocal
from .models.users import User
from sqlalchemy.exc import MultipleResultsFound
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.exc import IntegrityError


def create_user(email: str, password: str) -> User:
    """
    Create a new user with the given email and password.

    :param email: Email of the user
    :param password: Password of the user
    :return: User object
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
        return db_user
    except IntegrityError as e:
        db.rollback()
        print(f"User with email {email} already exists: {e}")
        raise e
    except SQLAlchemyError as e:
        db.rollback()
        print(f"Error creating user with email {email}: {e}")
        raise e
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
        return user_match
    except MultipleResultsFound as e:
        print(f"Multiple users with {email} found: {e}")
    except SQLAlchemyError as e:
        print(f"Error getting user with email {email}: {e}")
    finally:
        db.close()


def list_users():
    pass


def update_user():
    pass


def delete_user():
    pass
