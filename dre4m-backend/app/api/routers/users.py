# From imports
from fastapi import APIRouter
from fastapi import HTTPException

# Local imports
from app.api.models.users_api_models import ApiUser
from app.services.user_service import create_user
from app.exceptions import UserAlreadyExistsError
from app.auth.tokens import create_access_token

router = APIRouter(
    prefix='/users',
    tags=['Users'],
    # dependencies=[Depends(get_token_header)] This execs the function before
    # each endpoint, e.g: for token validation
)


@router.get("/")
async def get_users():
    return {"user_example": "example"}


@router.post("/create")
async def create_user_endpoint(user: ApiUser):
    try:
        create_user(user.email, user.password)

        access_token = create_access_token(data={"sub": user.email})

        # Create refresh token

        return {"access_token": access_token}
    except UserAlreadyExistsError as e:
        raise HTTPException(status_code=400, detail=str(e))
