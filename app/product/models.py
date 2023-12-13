from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import ForeignKey, DOUBLE_PRECISION

from app.database import Base


class Product(Base):
    __tablename__ = "product"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[int] = mapped_column(ForeignKey("provider.id"))
    provider: Mapped[str]
    price: Mapped[float] = mapped_column(DOUBLE_PRECISION)
    quantity: Mapped[int]
