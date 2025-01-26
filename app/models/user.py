from sqlalchemy import String, BigInteger, Integer, Date, Time, ForeignKey, Enum
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database import Base
from models.books import Books
from models.reserved import Reserved
from app.models.reserved import *  
import enum

class User(Base):
    __tablename__ = 'users'
    __table_args__ = {'extend_existing': True}
    telegram_id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    first_name: Mapped[str] = mapped_column(String, nullable=False)  # Имя пользователя
    username: Mapped[str] = mapped_column(String, nullable=True)  # Telegram username
    school_nick: Mapped[str] = mapped_column(String, nullable=True)  # Telegram username
    # Связь с таблицей броней книг (один пользователь может иметь несколько заявок)
    book_donate:Mapped[list["Books"]] = relationship(back_populates="users")
    applications: Mapped[list["Reserved"]] = relationship(back_populates="users")