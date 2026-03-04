import asyncio
import aiosqlite
from database import DB_PATH

class BroadcastService:

    @staticmethod
    async def get_all_users():
        async with aiosqlite.connect(DB_PATH) as db:
            cursor = await db.execute(
                "SELECT telegram_id FROM players"
            )
            return [row[0] for row in await cursor.fetchall()]

    @staticmethod
    async def send_broadcast(bot, text: str):
        users = await BroadcastService.get_all_users()

        success = 0
        failed = 0

        for user_id in users:
            try:
                await bot.send_message(user_id, text)
                success += 1
                await asyncio.sleep(0.05)  # защита от флуда
            except:
                failed += 1

        return success, failed