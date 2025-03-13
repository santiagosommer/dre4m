# Imports
import os
import pytest
import psycopg2

# From imports

# SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.orm import sessionmaker

from app.db.models.users_models import Base, User
from app.exceptions import MissingEnvironmentVariableError
from dotenv import load_dotenv

load_dotenv()

# Missing password in the connection string
DB_USER = os.getenv("DB_USER")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

if not all([DB_USER, DB_HOST, DB_PORT, DB_NAME]):
    raise MissingEnvironmentVariableError(
        "Missing database environment variables.")

TEST_DATABASE_URL = f"postgresql://{DB_USER}@{DB_HOST}:{DB_PORT}/{DB_NAME}"


def create_database():
    # Connects with the default database
    conn = psycopg2.connect(
        dbname="postgres", user=DB_USER, host=DB_HOST, port=DB_PORT)

    # Can't create a database within a transaction, avoid this using autocommit
    conn.autocommit = True

    # Check if the database exists, if not, create it
    cur = conn.cursor()
    cur.execute(f"SELECT 1 FROM pg_database WHERE datname = '{DB_NAME}';")
    exists = cur.fetchone()
    if not exists:
        cur.execute(f"CREATE DATABASE {DB_NAME};")
        print(f"Database {DB_NAME} created.")
    else:
        print(f"Database {DB_NAME} already exists.")

    # Create defined models tables in the database
    engine = create_engine(TEST_DATABASE_URL, echo=False)
    Base.metadata.create_all(bind=engine)
    print(f'Created tables: {list(Base.metadata.tables.keys())}')


def drop_database():
    # Connects with the default database
    conn = psycopg2.connect(
        dbname="postgres", user=DB_USER, host=DB_HOST, port=DB_PORT)
    # Can't create a database within a transaction, avoid this using autocommit
    conn.autocommit = True
    # Check if the database exists, if it does, drop it
    cur = conn.cursor()
    cur.execute(f"SELECT 1 FROM pg_database WHERE datname = '{DB_NAME}';")
    if cur.fetchone():
        # Terminate all connections to the database
        cur.execute(
            ("SELECT pg_terminate_backend(pid) "
             "FROM pg_stat_activity WHERE datname = %s;"),
            (DB_NAME,)
        )
        print(f"Connections to database {DB_NAME} terminated.")
        # Drop the database
        cur.execute(f"DROP DATABASE {DB_NAME};")
        print(f"Database {DB_NAME} deleted.")
    else:
        print(f"Database {DB_NAME} does not exist.")

    cur.close()
    conn.close()


@pytest.fixture(scope="session", autouse=True)
def setup_database():
    print("Setting up the database.")
    create_database()
    yield
    print("Tearing down the database.")
    drop_database()


@pytest.fixture(scope="function")
def db_session():
    """Creates a new session for each test"""
    engine = create_engine(TEST_DATABASE_URL, echo=False)
    TestingSessionLocal = sessionmaker(bind=engine)
    db: Session = TestingSessionLocal()
    print("Database session created.")
    yield db
    db.close()
    print("Database session closed.")


@pytest.fixture(scope="function")
def test_users():
    user1: User = User(email="test1@mail.com", password="test1")
    user2: User = User(email="test2@mail.com", password="test2")
    user3: User = User(email="test3@mail.com", password="test3")
    print("Test users created.")
    return user1, user2, user3
