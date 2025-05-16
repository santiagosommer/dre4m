from pydantic import BaseModel


class ApiToken(BaseModel):
    access_token: str
    token_type: str


class ApiTokenData(ApiToken):
    username: str | None = None
