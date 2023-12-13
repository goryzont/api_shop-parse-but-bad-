from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import  DOUBLE_PRECISION, Date
from datetime import date

from app.database import Base


class Delivery(Base):
    __tablename__ = "delivery"

    id: Mapped[int] = mapped_column(primary_key=True)
    date: Mapped[date] = mapped_column(Date)
    address: Mapped[str]
    price: Mapped[float] = mapped_column(DOUBLE_PRECISION)
