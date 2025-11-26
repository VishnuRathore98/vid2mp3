from pydantic import BaseModel, EmailStr
from sqlalchemy.types import DateTime


class User(BaseModel):
    user_id: str
    full_name: str
    email: EmailStr
    created_at: DateTime


class UserRegister(BaseModel):
    full_name: str
    email: EmailStr
    password: str


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class UserOut(BaseModel):
    user_id: str
    email: EmailStr


class UserUpdate(BaseModel):
    full_name: str | None = None
    email: EmailStr | None = None
    password: str | None = None
