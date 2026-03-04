import asyncio
from aiogram import Bot, Dispatcher
from config import BOT_TOKEN
from database import init_db

from handlers import start, admin, game
from handlers import broadcast
dp.include_router(broadcast.router)
async def main():
    init_db()

    bot = Bot(BOT_TOKEN)
    dp = Dispatcher()

    dp.include_router(start.router)
    dp.include_router(admin.router)
    dp.include_router(game.router)

    await dp.start_polling(bot)

if __name__ == "__main__":

    asyncio.run(main())
