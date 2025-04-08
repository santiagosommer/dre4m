# Imports
import os
import psycopg2
import sqlalchemy as sa
import psycopg2.sql as sql

# From imports
from sqlalchemy import create_engine
from dotenv import load_dotenv
from app.exceptions import MissingEnvironmentVariableError
from app.logging_config import logger
from app.db.models.user_models import Base

# For Base create_all table creation
from app.db.models.user_models import Customer
from app.db.models.order_models import Order
from app.db.models.product_models import Product
from app.db.models.address_models import Address


from sqlalchemy.orm import Session
from datetime import datetime, timezone


"""
This module contains utility functions for creating the database and tables.
"""

# Remove after developing the app
load_dotenv()

# Missing password in the connection string
DEFAULT_DB_USER = os.getenv("DEFAULT_DB_USER")
DB_NEW_USER = os.getenv("DB_USER")
DB_NEW_USER_PASSWORD = os.getenv("DB_USER_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

if not all([DEFAULT_DB_USER, DB_NEW_USER,
            DB_NEW_USER_PASSWORD, DB_HOST,
            DB_PORT, DB_NAME]):
    raise MissingEnvironmentVariableError("Missing environment variables")


def create_db_user():
    """
    Creates a database user if it does not exist.
    """
    conn = psycopg2.connect(
        dbname='postgres',
        user=DEFAULT_DB_USER,
        host=DB_HOST,
        port=DB_PORT
    )
    conn.autocommit = True
    cur = conn.cursor()

    # Check if the user already exists
    cur.execute(
        "SELECT 1 FROM pg_roles WHERE rolname = %s;", (DB_NEW_USER,)
    )
    exists = cur.fetchone()

    # Creates the user if it does not exist
    if not exists:
        cur.execute(
            sql.SQL(
                "CREATE USER {} WITH ENCRYPTED "
                "PASSWORD '{}' "
                "CREATEDB CREATEROLE REPLICATION BYPASSRLS LOGIN;").format(
                sql.Identifier(DB_NEW_USER),
                sql.Identifier(DB_NEW_USER_PASSWORD)
            )
        )
        logger.info(f"User {DB_NEW_USER} created.")
    else:
        logger.info(f"User {DB_NEW_USER} already exists.")

    cur.close()
    conn.close()


def create_db():
    """
    Creates the database if it does not exist.
    """
    try:
        # Connect to the database
        conn = psycopg2.connect(
            dbname="postgres",
            user=DB_NEW_USER,
            password=DB_NEW_USER_PASSWORD,
            host=DB_HOST,
            port=DB_PORT
        )
        conn.autocommit = True
        cur = conn.cursor()

        # Check if the database exists
        cur.execute(
            "SELECT 1 FROM pg_database WHERE datname = %s;", (DB_NAME,)
        )
        exists = cur.fetchone()

        # If the database does not exist, create it
        if not exists:
            cur.execute(
                sql.SQL("CREATE DATABASE {} OWNER {}").format(
                    sql.Identifier(DB_NAME),
                    sql.Identifier(DB_NEW_USER)
                )
            )
            # Revoke all privileges from the public role and grant connect and temporary privileges
            cur.execute(
                sql.SQL("REVOKE ALL PRIVILEGES ON DATABASE {} FROM PUBLIC;").format(
                    sql.Identifier(DB_NAME))
            )
            cur.execute(
                sql.SQL("GRANT CONNECT, CREATE ON DATABASE {} TO {};").format(
                    sql.Identifier(DB_NAME),
                    sql.Identifier(DB_NEW_USER)
                )
            )
            logger.info(f"Database {DB_NAME} created.")
        else:
            logger.info(f"Database {DB_NAME} already exists.")

        cur.close()
        conn.close()

    except Exception as e:
        logger.error(f"Error creating database: {e}")


def create_tables():
    """
    Creates the tables defined in the SQLAlchemy models.
    """
    DATABASE_URL = sa.URL.create(
        drivername="postgresql",
        username=DB_NEW_USER,
        password=DB_NEW_USER_PASSWORD,
        host=DB_HOST,
        port=DB_PORT,
        database=DB_NAME
    )
    engine = create_engine(DATABASE_URL, echo=False)
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    logger.info(f'Created tables: {list(Base.metadata.tables.keys())}')


def create_things():

    DATABASE_URL = sa.URL.create(
        drivername="postgresql",
        username=DB_NEW_USER,
        password=DB_NEW_USER_PASSWORD,
        host=DB_HOST,
        port=DB_PORT,
        database=DB_NAME
    )
    engine = create_engine(DATABASE_URL, echo=True)

    with Session(engine) as session:
        try:

            billing_address = Address(
                street_address="123 Billing St",
                address_info="Suite 1",
                city="New York",
                state_or_province="NY",
                zip_code="10001",
                country="USA",
                phone_number="1234567890"
            )

            shipping_address = Address(
                street_address="456 Shipping Ave",
                address_info="Apt 2B",
                city="Los Angeles",
                state_or_province="CA",
                zip_code="90001",
                country="USA",
                phone_number="0987654321"
            )

            product1 = Product(
                name="Product A",
                description="Description for Product A",
                price=10.0,
                stock=100,
                product_img="product_a.jpg"
            )

            product2 = Product(
                name="Product B",
                description="Description for Product B",
                price=20.0,
                stock=50,
                product_img="product_b.jpg"
            )

            order = Order(
                address=shipping_address,
                payment_method="Credit Card",
                total=30.0,
                order_date=datetime.now(timezone.utc),
                products=[product1, product2]
            )

            user = Customer(
                email="customer@example.com",
                password="securepassword",
                name="John",
                lastname="Doe",
                billing_address=billing_address,
                shipping_address=shipping_address,
                orders=[order]
            )

            session.add(user)

            session.commit()
            print("Usuario, direcciones, orden y productos creados exitosamente.")

        except Exception as e:
            session.rollback()
            print(f"Error al crear los datos: {e}")
