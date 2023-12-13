from pydantic import BaseModel, EmailStr


class SCustomer(BaseModel):
    name: str
    email: EmailStr
    phone: str
    state: int
    sysuser: int
