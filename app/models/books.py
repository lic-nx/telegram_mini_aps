from app.database import Base
from sqlalchemy import Column, Table
import enum
from sqlalchemy import String, BigInteger, Integer, Date, Time, ForeignKey, Enum, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship

# книги и типы книг например фантастика, программирование 
association_table = Table(
    "association_table",
    Base.metadata,
    Column("book_id", ForeignKey("books.book_id")),
    Column("author_id", ForeignKey("authtors.authtor_id")),
    extend_existing=True
)

class Types(Base):
    __tablename__ = "types"
    __table_args__ = {'extend_existing': True}
    type_id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    type_name: Mapped[str] = mapped_column(String)


class Books(Base):
    __tablename__ = "books"
    __table_args__ = {'extend_existing': True}
    book_id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    book_name: Mapped[str] = mapped_column(String, nullable=False)
    # count: Mapped[str] = mapped_column(Integer, server_default=0) # число книг в библиотеке 
    applications: Mapped[list["Types"]] = relationship(back_populates="books")
    is_reserved:Mapped[bool] = mapped_column(Boolean)