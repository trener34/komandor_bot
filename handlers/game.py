from aiogram import Router, F
from aiogram.types import CallbackQuery
from services.game_service import GameService
from services.list_builder import build_game_text

router = Router()


@router.callback_query(F.data.startswith("go_"))
async def go_handler(callback: CallbackQuery):

    game_id = int(callback.data.split("_")[1])
    result = await GameService.add_registration(game_id, callback.from_user.id)

    if result == "closed":
        await callback.answer("Игра уже закрыта", show_alert=True)
        return

    game = await GameService.get_active_game()
    players = await GameService.get_full_list(game_id)
    text = build_game_text(game[1], players)

    await callback.bot.edit_message_text(
        text,
        chat_id=game[2],
        message_id=game[3]
    )

    await callback.answer("Вы записаны ✅")


@router.callback_query(F.data.startswith("no_"))
async def no_handler(callback: CallbackQuery):

    game_id = int(callback.data.split("_")[1])
    await GameService.remove_registration(game_id, callback.from_user.id)

    game = await GameService.get_active_game()
    players = await GameService.get_full_list(game_id)
    text = build_game_text(game[1], players)

    await callback.bot.edit_message_text(
        text,
        chat_id=game[2],
        message_id=game[3]
    )

    await callback.answer("Вы снялись ❌")
