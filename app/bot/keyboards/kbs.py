from aiogram.types import ReplyKeyboardMarkup, WebAppInfo, InlineKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder
from app.config import settings

def main_keyboard(user_id: int, first_name: str)->ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    url_applications = f"{settings.BASE_SITE}/applications?user_id={user_id}"
    url_add_application = f'{settings.BASE_SITE}/form?user_id&first_name={first_name}'
    kb.button(text="Взятые мной книги", web_app=WebAppInfo(url=url_applications))
    kb.button(text="взять книгу", web_app=WebAppInfo(url=url_add_application))
    kb.button(text="у кого книга" )#TODO добавить поиск у кого книга
    if user_id == settings.ADNIN_ID:
        kb.button(text="Админ панель")
    kb.adjust(1)
    return kb.as_markup(resize_keyboard=True)
    