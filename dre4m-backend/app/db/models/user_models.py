# From imports
# SQLAlchemy
from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey
)
from sqlalchemy.orm import relationship

from typing import List, Optional
from app.db.connection import Base
from app.db.models.address_models import Address
from app.db.models.order_models import Order

# Table definition for users


class User(Base):
    # Table name in the database
    __tablename__ = 'users'

    # Columns in the table
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)

    # Indicate that Admin and Customer are subclasses of User
    __mapper_args__ = {
        'polymorphic_identity': 'user'
    }

    def __init__(self, email: str, password: str):
        self.email = email
        self.password = password


class Admin(User):
    # Table name in the database
    __tablename__ = 'admins'

    # Columns in the table
    id = Column(Integer, ForeignKey('users.id'), primary_key=True)

    # Link the Admin to the User
    user = relationship("User", back_populates="admin")

    # Indicate that Admin is a subclass of User
    __mapper_args__ = {
        'polymorphic_identity': 'admin',
    }

    def __init__(self, email: str, password: str, role: str):
        super().__init__(email, password)


class Customer(User):
    # Table name in the database
    __tablename__ = 'customers'

    # Columns in the table
    id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    name = Column(String)
    lastname = Column(String)

    # Relationships with Address
    billing_address_id = Column(
        Integer, ForeignKey('addresses.id'), nullable=True
    )
    shipping_address_id = Column(
        Integer, ForeignKey('addresses.id'), nullable=True
    )

    billing_address = relationship(
        "Address",
        foreign_keys=[billing_address_id],
        back_populates="customer_billing"
    )
    shipping_address = relationship(
        "Address",
        foreign_keys=[shipping_address_id],
        back_populates="customer_shipping"
    )

    # Relationships with Orders
    orders = relationship("Order", back_populates="customer")

    # Link the Customer to the User
    user = relationship("User", back_populates="customer")

    # Indicate that Customer is a subclass of User
    __mapper_args__ = {
        'polymorphic_identity': 'customer',
    }

    def __init__(self,
                 email: str, password: str,
                 name: str, lastname: str,
                 billing_address: Optional[Address] = None,
                 shipping_address: Optional[Address] = None,
                 orders: List[Order] = []
                 ):
        super().__init__(email, password)
        self.name = name
        self.lastname = lastname
        self.billing_address = billing_address
        self.shipping_address = shipping_address
        self.orders = orders or []


# Add reverse relationships in the parent class if needed
User.admin = relationship("Admin", uselist=False, back_populates="user")
User.customer = relationship("Customer", uselist=False, back_populates="user")
