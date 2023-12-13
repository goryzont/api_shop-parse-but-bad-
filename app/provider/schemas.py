from pydantic import BaseModel, EmailStr


class SProvider(BaseModel):
    name: str
    phone: str
    email: EmailStr
    address: str



