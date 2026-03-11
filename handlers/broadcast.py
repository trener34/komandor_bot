from aiogram import Router
from aiogram.types import Message
from services.broadcast_service import BroadcastService

router = Router()
broadcast_service = BroadcastService()

@router.message(commands=["broadcast"])
async def broadcast(message: Message):
    subs = broadcast_service.get_subscribers()
    await message.answer(f"Подписчики: {len(subs)}")
