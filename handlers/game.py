from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

router = Router()


@router.message(Command("new_game"))
async def new_game(message: Message):

    await message.answer(
        "🎮 Новая игра создана!"
    )


@router.message(Command("upload_list"))
async def upload_list(message: Message):

    await message.answer(
        "📂 Загрузка списка игроков."
    )
