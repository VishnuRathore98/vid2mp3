from pydantic import BaseModel, EmailStr
from datetime import datetime
from uuid import UUID


class User(BaseModel):
    user_id: str
    full_name: str
    email: EmailStr
    created_at: datetime


class UserRegister(BaseModel):
    full_name: str
    email: EmailStr
    password: str


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class UserOut(BaseModel):
    id: UUID
    email: EmailStr


class UserUpdate(BaseModel):
    full_name: str | None = None
    email: EmailStr | None = None
    password: str | None = None
