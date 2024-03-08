import asyncio
import os
import random
from pathlib import Path
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from dotenv import load_dotenv
from os import getenv
import logging


load_dotenv()
bot = Bot(token=getenv("BOT_TOKEN"))
dp = Dispatcher()


@dp.message(Command("start"))
async def start(message: types.Message):
    logging.info(message.from_user)
    (await message.answer(f"Привет, {message.from_user.first_name}!"))

@dp.message(Command("myinfo"))
async def myinfo(message: types.Message):
    logging.info(message.from_user)
    await message.answer(f"Ваш id: {message.from_user.id}!\n"
                         f"Ваш ник: {message.from_user.username}!\n"
                         f"Ваше имя: {message.from_user.first_name}!\n")


@dp.message(Command("random_pic"))
async def send_random_pic(message: types.Message):
    photos = os.listdir(Path("images"))
    file = types.FSInputFile(random.choice(photos))
    await message.answer_photo(file, caption="Котик")


@dp.message()
async def echo(message: types.Message):
    await message.answer(message.text)


async def main():
    # запуск бота
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())