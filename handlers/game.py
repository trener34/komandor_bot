from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

router = Router()

@router.message(Command("game"))
async def start_game(message: Message):

    await message.answer(
        "🎮 Игра началась!\n\n"
        "Скоро здесь будет игровая логика."
    )
