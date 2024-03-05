import asyncio
from aiogram import Bot, Dispatcher, types
from dotenv import load_dotenv
from os import getenv
import logging

load_dotenv()
bot = Bot(token=getenv("BOT_TOKEN"))
dp = Dispatcher()


@dp.message()
async def echo(message: types.Message):
    await message.answer("Привет")
    await message.answer(message.text)




async def main():
    # запуск бота
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())