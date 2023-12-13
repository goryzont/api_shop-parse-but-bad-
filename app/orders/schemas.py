from pydantic import BaseModel

from datetime import date


class SOrders(BaseModel):
    customer: int
    state: int
    delivery: int
    sum: float
    date: date


class SOrderProduct(BaseModel):
    order: int
    product: int
    quantity: int


class SOrderStates(BaseModel):
    name: str
