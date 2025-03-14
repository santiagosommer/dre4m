# From imports
# SQLAlchemy
from sqlalchemy import (
    Column,
    Integer,
    String
)
from sqlalchemy.orm import relationship
from app.db.connection import Base


# Table definition for address
class Address(Base):
    __tablename__ = 'addresses'

    # Columns in the table
    id = Column(Integer, primary_key=True, index=True)
    street_address = Column(String)
    extra_address = Column(String)
    city = Column(String)
    state_or_province = Column(String)
    zip_code = Column(String)
    country = Column(String)
    phone_number = Column(String)

    # Relationship back to Customer
    customer_billing = relationship("Customer",
                                    back_populates="billing_address",
                                    uselist=False)
    customer_shipping = relationship("Customer",
                                     back_populates="shipping_address",
                                     uselist=False)
