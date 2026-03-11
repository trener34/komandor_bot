class GameService:
    def __init__(self):
        self.games = {}

    def start_game(self, user_id):
        self.games[user_id] = {"score": 0}
        return "Игра началась!"

    def end_game(self, user_id):
        if user_id in self.games:
            score = self.games[user_id]["score"]
            del self.games[user_id]
            return f"Игра окончена. Ваш счет: {score}"
        return "Вы не играли."
