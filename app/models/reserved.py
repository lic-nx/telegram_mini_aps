from app.database import Base
from sqlalchemy import Column, Table
import enum
from sqlalchemy import String, Date, BigInteger, Integer, Date, Time, ForeignKey, Enum, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship

# таблица броней какой пользователь когда взял книгу и когда ее вернул
# кто взял, когда взял, что взял, когда должен вернуть. вернул ли книгу 
class Reserved(Base):
    __tablename__ = "reserved"
    __table_args__ = {'extend_existing': True}
    id:Mapped[int] = mapped_column(Integer, primary_key=True,autoincrement=True)
    telegram_id:Mapped[int] = mapped_column(Integer, ForeignKey('users.telegram_id')) # пользовате
    book_id:Mapped[int] = mapped_column(Integer, ForeignKey('books.book_id')) # книги
    to_take_date: Mapped[Date] = mapped_column(Date, nullable=False) # дата взятия книги
    to_return_date:Mapped[Date] = mapped_column(Date) # дата до которой надо вернуть книгу
    is_returned:Mapped[bool] = mapped_column(Boolean) # возвращено ли 
   
