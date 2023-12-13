from pydantic import BaseModel

from datetime import date


class SDelivery(BaseModel):
    date: date
    address: str
    price: float
