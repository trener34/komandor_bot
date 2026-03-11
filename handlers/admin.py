# получаем список по имени
cursor = await db.execute("""
    SELECT telegram_id FROM invite_list_members
    WHERE list_id=?
    ORDER BY position ASC
""", (list_id,))
users = await cursor.fetchall()

for user in users:
    await bot.send_message(
        user[0],
        f"🏐 Игра {date}\nПодтверди участие:",
        reply_markup=confirm_keyboard(game_id)
    )

    await asyncio.sleep(0.2)
