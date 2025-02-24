# методы для работы пользователя
from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message
from app.dao import UserDAO
from app.bot.keyboards.kbs import app_keyboard
from app.bot.utils.utils import greet_user, get_about_us_text

user_router = Router()

@user_router.message(CommandStart())
async def cmd_start(message: Message) -> None:
    """Обработка команды старт """
    user = await UserDAO