from pydantic import BaseModel, EmailStr
from enum import Enum


class UserRole(str, Enum):
    user = "user"
    manager = "manager"
    admin = "admin"


class SUserAuth(BaseModel):
    email: EmailStr
    password: str


class SUser(SUserAuth):
    role: UserRole
