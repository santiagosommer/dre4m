from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime, Table
from sqlalchemy.orm import relationship
from app.db.connection import Base
from app.db.models.product_models import Product
from datetime import datetime, timezone


class Order(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(Integer, ForeignKey('customers.id'))
    payment_method = Column(String)
    total_cost = Column(Float)
    order_date = Column(DateTime, default=lambda: datetime.now(timezone.utc))

    # Relationship with Customer
    customer = relationship("Customer", back_populates="orders")

    # Relationship with Product
    products = relationship(
        "Product", secondary="order_products", back_populates="orders")


# Association table for many-to-many relationship between Order and Product
order_products = Table(
    'order_products', Base.metadata,
    Column('order_id', Integer, ForeignKey('orders.id')),
    Column('product_id', Integer, ForeignKey('products.id'))
)
