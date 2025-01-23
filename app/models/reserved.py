from app.models.authtors import association_table
from database import Base
from sqlalchemy import Column, Table
import enum
from sqlalchemy import String, BigInteger, Integer, Date, Time, ForeignKey, Enum
from sqlalchemy.orm import Mapped, mapped_column, relationship

# таблица броней какой пользователь когда взял книгу и когда ее вернул
class Reserved(Base):
    __tablename__ = "reserved"
    id:Mapped = mapped_column(Integer, primary key)