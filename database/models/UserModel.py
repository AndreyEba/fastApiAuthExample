from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from database.models import Base

class UserModel(Base):
    __tablename__ = 'users'

    password: Mapped[str] = mapped_column()
    username: Mapped[str] = mapped_column(unique=True)
    email: Mapped[str] = mapped_column(unique=True)
    phone_number: Mapped[str] = mapped_column(unique=True)