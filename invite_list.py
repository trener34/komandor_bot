from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from config import ADMIN_ID
import aiosqlite
from database import DB_PATH

router = Router()


class UploadList(StatesGroup):
    waiting_for_list = State()


@router.message(F.text.startswith("/upload_list"))
async def start_upload(message: Message, state: FSMContext):
    if message.from_user.id != ADMIN_ID:
        return

    list_name = message.text.replace("/upload_list ", "")
    await state.update_data(list_name=list_name)
    await state.set_state(UploadList.waiting_for_list)

    await message.answer("Отправьте список никнеймов (@username), каждый с новой строки.")


@router.message(UploadList.waiting_for_list)
async def save_list(message: Message, state: FSMContext):
    data = await state.get_data()
    list_name = data["list_name"]

    usernames = message.text.splitlines()

    async with aiosqlite.connect(DB_PATH) as db:
        cursor = await db.execute(
            "INSERT INTO invite_lists (name) VALUES (?)",
            (list_name,)
        )
        list_id = cursor.lastrowid

        position = 1

        for username in usernames:
            username = username.strip().replace("@", "")

            # ищем пользователя в players
            cursor = await db.execute(
                "SELECT telegram_id FROM players WHERE name LIKE ?",
                (f"%{username}%",)
            )
            row = await cursor.fetchone()

            if row:
                await db.execute(
                    "INSERT INTO invite_list_members VALUES (?, ?, ?)",
                    (list_id, row[0], position)
                )
                position += 1

        await db.commit()

    await state.clear()
    await message.answer("Список сохранён ✅")