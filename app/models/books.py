from app.models.authtors import association_table
from database import Base
from sqlalchemy import Column, Table
import enum
from sqlalchemy import String, BigInteger, Integer, Date, Time, ForeignKey, Enum
from sqlalchemy.orm import Mapped, mapped_column, relationship

# книги и типы книг например фантастика, программирование 

class Types(Base):
    __tablename__ = "types"
    type_id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    type_name: Mapped[str] = mapped_column(String, primary_key=True, autoincrement=True)


class Books(Base):
    __tablename__ = "books"
    book_id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    book_name: Mapped[str] = mapped_column(String, nullable=False)
    # count: Mapped[str] = mapped_column(Integer, server_default=0) # число книг в библиотеке 
    applications: Mapped[list["Types"]] = relationship(back_populates="books")