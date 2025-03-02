from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    __tablename__ = None

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()