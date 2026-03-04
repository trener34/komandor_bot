# models.py

from dataclasses import dataclass


# ==== ENUM СТАТУСЫ ====

class GameStatus:
    ACTIVE = "active"
    CLOSED = "closed"


class RegistrationStatus:
    MAIN = "main"
    RESERVE = "reserve"


# ==== DATA MODELS ====

@dataclass
class Player:
    id: int
    telegram_id: int
    name: str


@dataclass
class Game:
    id: int
    date: str
    status: str
    chat_id: int
    message_id: int


@dataclass
class Registration:
    game_id: int
    user_id: int
    status: str


@dataclass
class InviteList:
    id: int
    name: str


@dataclass
class InviteListMember:
    list_id: int
    telegram_id: int
    position: int