import os

# Сделал проект по архитектуре которую увидел во время стажировки. На счет MVC архитектуры ->
# могу показать приватную репозиторию по проекту который делал на Django

from aiogram import Bot, Dispatcher
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram import executor
import logging
from dotenv import load_dotenv

from src.domains.telegram import index

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
