from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

router = Router()

ADMIN_ID = 123456789  # сюда вставь свой Telegram ID

@router.message(Command("admin"))
async def admin_panel(message: Message):

    if message.from_user.id != ADMIN_ID:
        await message.answer("❌ Нет доступа")
        return

    await message.answer("⚙️ Админ панель открыта")
