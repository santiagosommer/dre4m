# Debt: create a test database for testing

# Imports
import pytest

# From imports
from app.db.user_crud import (
    create_user,
    get_user,
    delete_user)
from app.db.models.users_models import User
from sqlalchemy.exc import (
    IntegrityError,
    NoResultFound
)


# Fixture to create test users
@pytest.fixture(scope="function")
def test_users():
    user1: User = User(email="test1@mail.com", password="test1")
    user2: User = User(email="test2@mail.com", password="test2")
    user3: User = User(email="test3@mail.com", password="test3")
    return user1, user2, user3


def test_create_get_and_delete(test_users: tuple[User, User, User]):

    user1, user2, user3 = test_users

    # Create users
    create_user(str(user1.email), str(user1.password))
    create_user(str(user2.email), str(user2.password))
    assert get_user(str(user1.email)) is not None
    assert get_user(str(user2.email)) is not None

    # Delete an existent user
    delete_user(str(user1.email))
    assert get_user(str(user1.email)) is None

    # Create an existent user
    with pytest.raises(IntegrityError):
        create_user(str(user2.email), str(user2.password))
    assert get_user(str(user2.email)) is not None

    # Delete inexistent user
    with pytest.raises(NoResultFound):
        delete_user(str(user3.email))

    # Last checks
    assert get_user(str(user1.email)) is None
    assert get_user(str(user2.email)) is not None
    assert get_user(str(user3.email)) is None

    # Clean up
    delete_user(str(user2.email))
