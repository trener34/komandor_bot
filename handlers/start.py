from aiogram import Router
from aiogram.types import Message
from services.game_service import GameService

router = Router()

@router.message()
async def start_handler(message: Message):
    if message.text == "/start":
        await GameService.register_user(
            message.from_user.id,
            message.from_user.full_name
        )
        await message.answer("Вы зарегистрированы в системе 🏐")

