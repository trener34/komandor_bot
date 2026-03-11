import asyncio
from aiogram import Bot, Dispatcher
from config import BOT_TOKEN

from handlers.start import router as start_router
from handlers.admin import router as admin_router
from handlers.game import router as game_router
from handlers.broadcast import router as broadcast_router


async def main():
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()

    dp.include_router(start_router)
    dp.include_router(admin_router)
    dp.include_router(game_router)
    dp.include_router(broadcast_router)

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
