# From imports

# SQLAlchemy
from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey
)
from sqlalchemy.orm import relationship

from ..connection import Base


# Object definition for users
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
    role = Column(String)

    # Link the Admin to the User
    user = relationship("User", back_populates="admin")

    # Indicate that Admin is a subclass of User
    __mapper_args__ = {
        'polymorphic_identity': 'admin',
    }

    def __init__(self, email: str, password: str, role: str):
        super().__init__(email, password)
        self.role = role


class Customer(User):
    # Table name in the database
    __tablename__ = 'customers'

    # Columns in the table
    id = Column(Integer, ForeignKey('users.id'), primary_key=True)

    # Link the Customer to the User
    user = relationship("User", back_populates="customer")

    # Indicate that Customer is a subclass of User
    __mapper_args__ = {
        'polymorphic_identity': 'customer',
    }

    def __init__(self, email: str, password: str):
        super().__init__(email, password)


# Add reverse relationships in the parent class if needed
User.admin = relationship("Admin", uselist=False, back_populates="user")
User.customer = relationship("Customer", uselist=False, back_populates="user")
