from sqlalchemy.future import select
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import joinedload
from app.dao.base import BaseDAO
from app.models import user, reserved, books, authtors
from app.database import async_session_maker

class UserDAO(BaseDAO):
    model = user

class ReservedDAO(BaseDAO):
    model = reserved

    @classmethod
    async def get_reserved_by_users(cls, user_id: int):
        """
        Возвращает информацию обо всех взятых книгах пользователем определенным пользователем
        
        Аргументы:
            user_id: Идентификатор пользователя
        Возвращает:
            Список взятых книг, дата когда взяли, когда вернули/должны были вернуть, Возвращена ли книга 
        """
        async with async_session_maker() as session:
            try:
                query = (
                    select(cls.model)
                    .optins(joinedload(cls.model.User), joinedload(cls.model.Books))
                    .filter_by(user_id = user_id)
                )
                result = await session.execute(query)
                applications = result.scalars().all()

                return[
                    {
                        "book_name": app.book_name,
                        "to_take_date": app.to_take_date,
                        "to_return_date": app.to_return_date,
                        "is_returned":app.is_returned
                    }
                    for app in applications
                ]
            except SQLAlchemyError as e:
                print(f"Error while fetching applications for user {user_id}: {e}")
                return None

    @classmethod
    async def get_books_to_return(cls):
        """
        Возвращает информацию обо всех взятых книгах которые еще не вернули 
        
        Аргументы:
            
        Возвращает:
            Список взятых книг, дата когда взяли, когда вернули/должны были вернуть, Возвращена ли книга 
        """
        async with async_session_maker() as session:
            try:
                query = (
                    select(cls.model)
                    .optins(joinedload(cls.model.User), joinedload(cls.model.Books))
                    .filter_by(is_returned = False)
                )
                result = await session.execute(query)
                applications = result.scalars().all()

                return[
                    {
                        "book_name": app.book_name,
                        "to_take_date": app.to_take_date,
                        "to_return_date": app.to_return_date,
                        "is_returned":app.is_returned
                    }
                    for app in applications
                ]
            except SQLAlchemyError as e:
                print(f"Error while fetching applications for user {user_id}: {e}")
                return None


class BooksDAO(BaseDAO):
    model = books

class AuthtorsDAO(BaseDAO):
    model = authtors
    