
from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import ForeignKey, Date, DOUBLE_PRECISION, JSON
from datetime import date

from app.database import Base
from app.delivery.models import Delivery


class Orders(Base):
    __tablename__ = "orders"

    id: Mapped[int] = mapped_column(primary_key=True)
    customer: Mapped[int] = mapped_column(ForeignKey("customer.id"))
    state: Mapped[int] = mapped_column(ForeignKey("order_states.id"))
    delivery: Mapped[int] = mapped_column(ForeignKey("delivery.id"))
    sum: Mapped[float] = mapped_column(DOUBLE_PRECISION)
    date: Mapped[date] = mapped_column(Date)


class OrderProduct(Base):
    __tablename__ = "order_product"

    id: Mapped[int] = mapped_column(primary_key=True)
    order: Mapped[int] = mapped_column(ForeignKey("orders.id"))
    product: Mapped[int] = mapped_column(ForeignKey("product.id"))
    quantity: Mapped[int]


class OrderStates(Base):
    __tablename__ = "order_states"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
