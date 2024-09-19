from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from enum import Enum


class SubType(str, Enum):
    member = "member"
    guest = "guest"


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    is_member: Mapped[SubType] = mapped_column(nullable=True)


class Bundle(Base):
    __tablename__ = 'bundles'

    id: Mapped[int] = mapped_column(primary_key=True)
    link: Mapped[str] = mapped_column(nullable=False)