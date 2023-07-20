import os

from aiogram import Bot, Dispatcher, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher import FSMContext
from aiogram.types import ParseMode
from aiogram import executor
import logging
from dotenv import load_dotenv

from domains.telegram import index

load_dotenv()

API_TOKEN = os.getenv('API_TOKEN')

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())

dp.register_message_handler(index.cmd_start, commands=['start'], state="*")
dp.register_message_handler(index.cmd_add, commands=['add'], state="*")
dp.register_message_handler(index.cmd_done, commands=['done'], state="*")
dp.register_message_handler(index.cmd_list, commands=['list'], state="*")
dp.register_message_handler(index.cmd_delete, commands=['delete'], state="*")

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)
