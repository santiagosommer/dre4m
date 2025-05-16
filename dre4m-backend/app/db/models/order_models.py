# From imports
from sqlalchemy import (
    Column,
    Integer,
    String,
    Float,
    ForeignKey,
    DateTime,
    Table
)
from sqlalchemy.orm import relationship
from datetime import datetime, timezone

# Local imports
from ...db.connection import Base
from .product_models import Product  # Order mapper needs this import


class Order(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(Integer, ForeignKey('customers.id'))
    address_id = Column(Integer, ForeignKey('addresses.id'))
    payment_method = Column(String)
    total = Column(Float)
    order_date = Column(DateTime, default=lambda: datetime.now(timezone.utc))

    # Relationship with Customer
    customer = relationship("Customer", back_populates="orders")

    # Relationship with Product
    products = relationship(
        "Product", secondary="order_products", back_populates="orders")

    # Relationship with address
    address = relationship("Address", back_populates="orders")


# Association table for many-to-many relationship between Order and Product
order_products = Table(
    'order_products', Base.metadata,
    Column('order_id', Integer, ForeignKey('orders.id')),
    Column('product_id', Integer, ForeignKey('products.id'))
)
