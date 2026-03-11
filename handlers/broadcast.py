from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

router = Router()

@router.message(Command("broadcast"))
async def broadcast(message: Message):

    await message.answer(
        "📢 Функция рассылки пока в разработке."
    )
