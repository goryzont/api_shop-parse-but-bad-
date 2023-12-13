from pydantic import BaseModel


class SProduct(BaseModel):
    name: str
    provider: int
    price: float
    quantity: int
