from pydantic import BaseModel, field_validator


class Item(BaseModel):
    id: int
    name: str
    supplier: str  # provider
    salePriceU: float  # price
    volume: int  # quantity

    @field_validator('salePriceU')
    def convert_sale_price(cls, sale_price: int) -> float:
        if sale_price is not None:
            return sale_price / 100


class Items(BaseModel):
    products: list[Item]