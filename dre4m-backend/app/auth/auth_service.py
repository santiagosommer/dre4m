# From imports
from ..exceptions import NotAuthorizedUserError
from .security import authenticate_user
from .tokens import (
    create_access_token,
    decode_token
)


def login_user(form_email: str, form_password: str):
    authorized_user = authenticate_user(form_email, form_password)

    if not authorized_user:
        raise NotAuthorizedUserError(f"Auth failed for: {form_email}")

    access_token = create_access_token(data={"sub": form_email})

    return access_token


def decode_access_token(access_token: str):
    return decode_token(access_token)
