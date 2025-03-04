# From imports
from sqlalchemy.orm import Session
from sqlalchemy import select
from .connection import SessionLocal
from .models.users import User
from sqlalchemy.exc import MultipleResultsFound
from sqlalchemy.exc import SQLAlchemyError


def create_user(email: str, password: str):
    pass


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
    db: Session = SessionLocal()
    pass


def update_user():
    db: Session = SessionLocal()
    pass


def delete_user():
    db: Session = SessionLocal()
    pass


# Test the function
print(get_user('nuevo_usuario@example.com'))
