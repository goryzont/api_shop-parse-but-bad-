from sqlalchemy import select, update
from fastapi import Body

from app.dao.base import BaseDAO
from app.database import async_session_maker
from app.provider.models import Provider
from app.provider.schemas import SProvider


class ProviderDAO(BaseDAO):
    model = Provider

    @classmethod
    async def update(cls, provider_id: int, provider: SProvider):
        async with async_session_maker() as session:
            query = update(cls.model).filter_by(id=provider_id).values(name=provider.name, phone=provider.phone,
                                                                       email=provider.email, address=provider.address)
            await session.execute(query)
            await session.commit()






