from aiogram import Router
from aiogram.types import Message
from services.game_service import GameService

router = Router()
game_service = GameService()

@router.message(commands=["startgame"])
async def start_game(message: Message):
    text = game_service.start_game(message.from_user.id)
    await message.answer(text)

@router.message(commands=["endgame"])
async def end_game(message: Message):
    text = game_service.end_game(message.from_user.id)
    await message.answer(text)
