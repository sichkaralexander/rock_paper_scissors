from aiogram import Bot, Dispatcher
from config_data.config import Config, load_config
from handlers import other_handlers, user_handlers

config : Config = load_config() 
bot : Bot = Bot(config.token.tg_bot)
dp : Dispatcher = Dispatcher()

dp.include_router(user_handlers.router)
dp.include_router(other_handlers.router)

if __name__ == '__main__':
    dp.run_polling(bot)