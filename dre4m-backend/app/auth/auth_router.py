# From imports
from fastapi import (
    APIRouter,
    HTTPException,
    status,
    Response,
    Request
)
from fastapi.responses import JSONResponse
# Local imports
from app.auth.auth_service import (
    login_user,
    decode_access_token
)
from app.exceptions import NotAuthorizedUserError
from app.api.models.users_api_models import ApiUser
from settings.settings import get_settings

settings = get_settings()

router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)


@router.post("/token")
async def login_for_access_token(form_data: ApiUser, response: Response):
    try:
        access_token = login_user(form_data.email, form_data.password)

        response = JSONResponse(content={"message": "Login successful"})
        response.set_cookie(
            key="access_token",
            value=access_token,
            httponly=True,
            secure=settings.IS_PRODUCTION,
            samesite="lax",
            max_age=60 * 60,
            path="/"
        )

        return response
    except NotAuthorizedUserError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    except Exception as e:
        print(e)


@router.get("/me")
async def get_cookie_token(request: Request):
    token = request.cookies.get("access_token")

    if not token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Not authenticated",
            headers={"WWW-Authenticate": "Bearer"}
        )
    return token
