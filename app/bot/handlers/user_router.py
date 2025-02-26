# методы для работы пользователя
from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message
from app.dao.dao import UserDAO
from app.bot.keyboards.kbs import app_keyboard
from app.bot.utils.utils import greet_user

user_router = Router()

@user_router.message(CommandStart())
async def cmd_start(message: Message) -> None:
    """Обработка команды старт """
    user = await UserDAO.find_one_or_none(telegram_id=message.from_user.id)
    if not user:
        await UserDAO.add(
            telegram_id=message.from_user.id,
            first_name=message.from_user.first_name,
            username=message.from_user.username
        )
    await greet_user(message, is_new_user=not user)

@user_router.message(F.text == '🔙 Назад')
async def cmd_back_home(message: Message) -> None:
    """Обработка команды назад"""
    await greet_user(message, is_new_user=False)

