from pydantic import BaseModel, EmailStr


# Object definition for users
class User(BaseModel):
    email: EmailStr
    password: str


class Admin(User):
    role: str


class Customer(User):
    pass
