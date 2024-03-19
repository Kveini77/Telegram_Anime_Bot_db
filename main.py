import asyncio
import logging

from aiogram import Dispatcher
from aiogram import Bot

from bot import bot, dp, db
from handlers.start import start_router
from handlers.shop import shop_router
from handlers.reviews import reviews_router
from handlers.survey import survey_router


async def on_startup(bot: Bot):
    db.drop_tables()
    db.create_table()
    db.populate_tables()


async def main():
    # Регитсрация роутеров
    dp.include_router(shop_router)
    dp.include_router(start_router)
    dp.include_router(reviews_router)
    dp.include_router(survey_router)

    dp.startup.register(on_startup)
    # запуск бота
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())