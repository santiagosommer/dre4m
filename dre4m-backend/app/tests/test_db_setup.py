# Imports
import pytest

# From imports
from sqlalchemy import inspect
from sqlalchemy.orm import Session


# These should be the first tests to run

# Check if the tables exists
@pytest.mark.order(1)
def test_database_setup(db_session: Session):
    print("Testing database setup.")
    # Verify that the session is bound to the engine
    assert db_session.bind is not None, \
        "Database session bind should not be None"
    # Verify that the table 'users' exists with the inspector
    inspector = inspect(db_session.bind)
    assert inspector.has_table("users"), "Table 'users' should exist"
