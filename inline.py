from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def confirm_keyboard(game_id: int):
    return InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="✅ Иду", callback_data=f"go_{game_id}"),
            InlineKeyboardButton(text="❌ Не иду", callback_data=f"no_{game_id}")
        ]
    ])