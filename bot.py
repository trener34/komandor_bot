import asyncio
from aiogram import Bot, Dispatcher
from config import BOT_TOKEN
from database import init_db
from handlers import start, admin, game, broadcast

async def main():
    # Инициализация базы данных
    await init_db()

    # Создаем бот и диспетчер
    bot = Bot(token=BOT_TOKEN, parse_mode="HTML")
    dp = Dispatcher()

    # Подключаем роутеры
    dp.include_router(start.router)
    dp.include_router(admin.router)
    dp.include_router(game.router)
    dp.include_router(broadcast.router)

    # Запускаем бот
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
