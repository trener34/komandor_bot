import aiosqlite
from config import MAX_PLAYERS
from database import DB_PATH


class GameService:

    @staticmethod
    async def register_user(telegram_id, name):
        async with aiosqlite.connect(DB_PATH) as db:
            await db.execute(
                "INSERT OR IGNORE INTO players (telegram_id, name) VALUES (?, ?)",
                (telegram_id, name)
            )
            await db.commit()

    @staticmethod
    async def create_game(date, chat_id):
        async with aiosqlite.connect(DB_PATH) as db:
            cursor = await db.execute(
                "INSERT INTO games (date, status, chat_id) VALUES (?, ?, ?)",
                (date, "active", chat_id)
            )
            await db.commit()
            return cursor.lastrowid

    @staticmethod
    async def close_game(game_id):
        async with aiosqlite.connect(DB_PATH) as db:
            await db.execute(
                "UPDATE games SET status='closed' WHERE id=?",
                (game_id,)
            )
            await db.commit()

    @staticmethod
    async def get_active_game():
        async with aiosqlite.connect(DB_PATH) as db:
            cursor = await db.execute(
                "SELECT id, date, chat_id, message_id FROM games WHERE status='active' ORDER BY id DESC LIMIT 1"
            )
            return await cursor.fetchone()

    @staticmethod
    async def set_message_id(game_id, message_id):
        async with aiosqlite.connect(DB_PATH) as db:
            await db.execute(
                "UPDATE games SET message_id=? WHERE id=?",
                (message_id, game_id)
            )
            await db.commit()

    @staticmethod
    async def add_registration(game_id, user_id):

        async with aiosqlite.connect(DB_PATH) as db:

            # проверка закрытия
            cursor = await db.execute(
                "SELECT status FROM games WHERE id=?",
                (game_id,)
            )
            status = (await cursor.fetchone())[0]
            if status != "active":
                return "closed"

            # считаем основной состав
            cursor = await db.execute("""
                SELECT COUNT(*) FROM registrations
                WHERE game_id=? AND status='main'
            """, (game_id,))
            count = (await cursor.fetchone())[0]

            role = "main" if count < MAX_PLAYERS else "reserve"

            await db.execute("""
                DELETE FROM registrations
                WHERE game_id=? AND user_id=?
            """, (game_id, user_id))

            await db.execute("""
                INSERT INTO registrations (game_id, user_id, status)
                VALUES (?, ?, ?)
            """, (game_id, user_id, role))

            await db.commit()

            return role

    @staticmethod
    async def remove_registration(game_id, user_id):
        async with aiosqlite.connect(DB_PATH) as db:

            await db.execute("""
                DELETE FROM registrations
                WHERE game_id=? AND user_id=?
            """, (game_id, user_id))

            # перенос из резерва
            cursor = await db.execute("""
                SELECT user_id FROM registrations
                WHERE game_id=? AND status='reserve'
                ORDER BY created_at ASC
                LIMIT 1
            """, (game_id,))
            row = await cursor.fetchone()

            if row:
                await db.execute("""
                    UPDATE registrations
                    SET status='main'
                    WHERE game_id=? AND user_id=?
                """, (game_id, row[0]))

            await db.commit()

    @staticmethod
    async def get_full_list(game_id):
        async with aiosqlite.connect(DB_PATH) as db:
            cursor = await db.execute("""
                SELECT p.name, r.status
                FROM registrations r
                JOIN players p ON p.telegram_id=r.user_id
                WHERE r.game_id=?
                ORDER BY r.created_at ASC
            """, (game_id,))
            return await cursor.fetchall()