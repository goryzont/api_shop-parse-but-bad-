from sqlalchemy import update

from app.dao.base import BaseDAO
from app.database import async_session_maker
from app.product.models import Product
from app.product.schemas import SProduct


class ProductDAO(BaseDAO):
    model = Product

    @classmethod
    async def update(cls, product_id: int, product: SProduct):
        async with async_session_maker() as session:
            query = update(cls.model).filter_by(id=product_id).values(name=product.name, provider=product.provider,
                                                                      price=product.price, quantity=product.quantity)
            await session.execute(query)
            await session.commit()
