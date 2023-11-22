from environs import Env
from dataclasses import dataclass
@dataclass
class TgBot:
    token: str

@dataclass
class Admin:
    id: str

@dataclass
class Config:
    bot: TgBot
    admin: Admin

def load_config(path=None) -> Config:
    env = Env()
    env.read_env()
    return Config(TgBot(token=env('BOT_TOKEN')),
                  Admin(id=env('ADMIN_ID')))

