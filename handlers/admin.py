from aiogram import Router
from aiogram.types import Message

router = Router()

@router.message(commands=["admin"])
async def cmd_admin(message: Message):
    await message.answer("Это админ-команда. Тут можно добавить управление ботом.")
