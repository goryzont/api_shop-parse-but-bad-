from sqlalchemy.orm import mapped_column, Mapped


from app.database import Base


class Provider(Base):
    __tablename__ = "provider"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    phone: Mapped[str]
    email: Mapped[str]
    address: Mapped[str]

