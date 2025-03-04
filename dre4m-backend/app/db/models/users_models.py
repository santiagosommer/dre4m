# From imports
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from ..connection import Base


# Object definition for users
class User(Base):
    __tablename__ = 'users'

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
    __tablename__ = 'admins'

    id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    role = Column(String)

    # Link the Admin to the User
    user = relationship("User", back_populates="admin")

    __mapper_args__ = {
        'polymorphic_identity': 'admin',
    }

    def __init__(self, email: str, password: str, role: str):
        super().__init__(email, password)
        self.role = role


class Customer(User):
    __tablename__ = 'customers'

    id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    # email = Column(String, unique=True)

    # Link the Customer to the User
    user = relationship("User", back_populates="customer")

    __mapper_args__ = {
        'polymorphic_identity': 'customer',
    }

    def __init__(self, email: str, password: str):
        super().__init__(email, password)
        # self.email = email


# Add reverse relationships in the parent class if needed
User.admin = relationship("Admin", uselist=False, back_populates="user")
User.customer = relationship("Customer", uselist=False, back_populates="user")
