from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from config import ADMIN_ID
from services.broadcast_service import BroadcastService

router = Router()


class BroadcastState(StatesGroup):
    waiting_text = State()
    confirm = State()


# Запуск рассылки
@router.message(F.text == "/broadcast")
async def start_broadcast(message: Message, state: FSMContext):
    if message.from_user.id != ADMIN_ID:
        return

    await state.set_state(BroadcastState.waiting_text)
    await message.answer("Введите текст для рассылки:")


# Получаем текст
@router.message(BroadcastState.waiting_text)
async def get_text(message: Message, state: FSMContext):
    await state.update_data(text=message.text)

    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="✅ Отправить", callback_data="confirm_broadcast"),
            InlineKeyboardButton(text="❌ Отмена", callback_data="cancel_broadcast")
        ]
    ])

    await state.set_state(BroadcastState.confirm)
    await message.answer(
        f"Предпросмотр:\n\n{message.text}\n\nОтправить?",
        reply_markup=keyboard
    )


# Подтверждение
@router.callback_query(F.data == "confirm_broadcast")
async def confirm(callback: CallbackQuery, state: FSMContext):
    if callback.from_user.id != ADMIN_ID:
        return

    data = await state.get_data()
    text = data["text"]

    await callback.message.edit_text("Рассылка запущена...")

    success, failed = await BroadcastService.send_broadcast(
        callback.bot, text
    )

    await callback.message.answer(
        f"✅ Успешно: {success}\n❌ Ошибок: {failed}"
    )

    await state.clear()


# Отмена
@router.callback_query(F.data == "cancel_broadcast")
async def cancel(callback: CallbackQuery, state: FSMContext):
    await state.clear()
    await callback.message.edit_text("Рассылка отменена.")