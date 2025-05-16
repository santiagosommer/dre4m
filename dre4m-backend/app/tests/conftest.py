# Imports
import os
import pytest
import psycopg2

# From imports

# SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.orm import sessionmaker

from dotenv import load_dotenv

# Local imports
from app.db.models.user_models import Base, User
from app.exceptions import MissingEnvironmentVariableError

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


# def create_things():
#     engine = create_engine(DATABASE_URL, echo=True)

#     # Crear una sesión
#     with Session(engine) as session:
#         try:

#             # Crear direcciones de envío y facturación
#             billing_address = Address(
#                 street_address="123 Billing St",
#                 address_info="Suite 1",
#                 city="New York",
#                 state_or_province="NY",
#                 zip_code="10001",
#                 country="USA",
#                 phone_number="1234567890"
#             )

#             shipping_address = Address(
#                 street_address="456 Shipping Ave",
#                 address_info="Apt 2B",
#                 city="Los Angeles",
#                 state_or_province="CA",
#                 zip_code="90001",
#                 country="USA",
#                 phone_number="0987654321"
#             )

#             # Crear productos
#             product1 = Product(
#                 name="Product A",
#                 description="Description for Product A",
#                 price=10.0,
#                 stock=100,
#                 product_img="product_a.jpg"
#             )

#             product2 = Product(
#                 name="Product B",
#                 description="Description for Product B",
#                 price=20.0,
#                 stock=50,
#                 product_img="product_b.jpg"
#             )

#             # Crear una orden asociada al usuario y a la dirección de envío
#             order = Order(
#                 address=shipping_address,
#                 payment_method="Credit Card",
#                 total=30.0,
#                 order_date=datetime.now(timezone.utc),
#                 products=[product1, product2]  # Asociar productos a la orden
#             )

#             # Crear un usuario
#             user = Customer(
#                 email="customer@example.com",
#                 password="securepassword",
#                 name="John",
#                 lastname="Doe",
#                 billing_address=billing_address,
#                 shipping_address=shipping_address,
#                 orders=[order]
#             )

#             # Agregar todo a la sesión
#             session.add(user)

#             # Confirmar los cambios
#             session.commit()
#             print("Usuario, direcciones, orden y productos creados exitosamente.")

#         except Exception as e:
#             session.rollback()
#             print(f"Error al crear los datos: {e}")
