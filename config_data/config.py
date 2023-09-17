from dataclasses import dataclass
from environs import Env


@dataclass
class Tg_Bot:
    tg_bot: str


@dataclass
class Config:
    token: Tg_Bot


def load_config():
    env = Env()
    env.read_env()
    return Config(token=Tg_Bot(tg_bot=env('TOKEN')))


