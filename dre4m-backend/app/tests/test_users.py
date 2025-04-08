# Imports
import pytest

# From imports
from app.db.user_crud import (
    crud_create_user,
    crud_get_user,
    crud_delete_user
)
from app.db.models.user_models import User
from sqlalchemy.orm import Session

from sqlalchemy.exc import (
    IntegrityError,
    NoResultFound
)


def test_crud_create_delete_users(
    db_session: Session, test_users: tuple[User, User, User]
):
    user1, user2, _ = test_users
    crud_create_user(db_session, str(user1.email), str(user1.password))
    crud_create_user(db_session, str(user2.email), str(user2.password))
    assert crud_get_user(db_session, str(user1.email)) is not None
    assert crud_get_user(db_session, str(user2.email)) is not None
    crud_delete_user(db_session, str(user1.email))
    crud_delete_user(db_session, str(user2.email))
    assert crud_get_user(db_session, str(user2.email)) is None


def test_create_existing_user(
        db_session: Session, test_users: tuple[User, User, User]
):
    _, user2, _ = test_users
    crud_create_user(db_session, str(user2.email), str(user2.password))
    with pytest.raises(IntegrityError):
        crud_create_user(db_session, str(user2.email), str(user2.password))
    assert crud_get_user(db_session, str(user2.email)) is not None
    crud_delete_user(db_session, str(user2.email))


def test_delete_nonexistent_user(
    db_session: Session, test_users: tuple[User, User, User]
):
    _, _, user3 = test_users
    with pytest.raises(NoResultFound):
        crud_delete_user(db_session, str(user3.email))
    assert crud_get_user(db_session, str(user3.email)) is None
