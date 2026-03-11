import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN не задан. Установите переменную окружения BOT_TOKEN")
ADMIN_ID = 184818027  # <-- твой telegram id
MAX_PLAYERS = 12
