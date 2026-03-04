def build_game_text(date, players):
    main = []
    reserve = []
    no = []

    for name, status in players:
        if status == "main":
            main.append(name)
        elif status == "reserve":
            reserve.append(name)
        else:
            no.append(name)

    text = f"🏐 Игра {date}\n\n"

    text += f"✅ Основной состав ({len(main)}/12):\n"
    for i, p in enumerate(main, 1):
        text += f"{i}. {p}\n"

    text += f"\n🕒 Резерв ({len(reserve)}):\n"
    for i, p in enumerate(reserve, 1):
        text += f"{i}. {p}\n"

    return text