from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship
from app.db.connection import Base


class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)
    price = Column(Float)

    # Relationship with Order
    orders = relationship(
        "Order", secondary="order_products", back_populates="products")
