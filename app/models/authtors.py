# у одной книги может быть несколько авторов а у одного автора несколько книг
from sqlalchemy import String, BigInteger, Integer, Date, Time, ForeignKey, Enum
from sqlalchemy.orm import Mapped, mapped_column, relationship
from models.books import Books
from app.database import Base
from sqlalchemy import Column, Table
import enum

# таблица для связи многие ко многим для авторов и книг
association_table = Table(
    "association_table",
    Base.metadata,
    Column("book_id", ForeignKey("books.book_id")),
    Column("author_id", ForeignKey("authtors.authtor_id"))
)

class Authtors(Base):
    __tablename__ = 'authtors'
    authtor_id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    auther_name: Mapped[str] = mapped_column(String, nullable=False) #имя автора

    applications: Mapped[list["Books"]] = relationship(secondary=association_table)