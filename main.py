import asyncio
import logging
from bot import bot, dp
from handlers.start import start_router
from handlers.shop import shop_router
from handlers.reviews import reviews_router


async def main():
    # Регитсрация роутеров
    dp.include_router(shop_router)
    dp.include_router(start_router)
    dp.include_router(reviews_router)
    # запуск бота
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())