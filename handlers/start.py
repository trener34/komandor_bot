from aiogram import Router
from aiogram.types import Message
from services.broadcast_service import BroadcastService

router = Router()
broadcast_service = BroadcastService()

@router.message(commands=["start"])
async def cmd_start(message: Message):
    broadcast_service.subscribe(message.from_user.id)
    await message.answer(f"Привет, {message.from_user.first_name}! Я работаю 🚀")
