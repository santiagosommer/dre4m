# From imports
from ..services.user_service import get_user
from ..api.models.users_api_models import ApiUser
from .hashing import verify_password


def authenticate_user(username: str, plain_password: str) -> ApiUser | None:
    api_user = get_user(username)

    if not api_user or not verify_password(api_user.password, plain_password):
        return None

    return api_user
