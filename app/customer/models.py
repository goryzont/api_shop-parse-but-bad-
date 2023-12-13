from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import ForeignKey, DOUBLE_PRECISION, Date
from datetime import date

from app.database import Base


class Customer(Base):
    __tablename__ = "customer"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    email: Mapped[str]
    phone: Mapped[str]
    state: Mapped[int] = mapped_column(ForeignKey("customer_states.id"))
    sysuser: Mapped[int] = mapped_column(ForeignKey("users.id"))


class CustomerStates(Base):
    __tablename__ = "customer_states"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
