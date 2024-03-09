from aiogram import Router, F, types
from aiogram.filters import Command
import logging
import random
from handlers.start import start_router
reviews_router = Router()


@start_router.callback_query(F.data == "reviews")
async def reviews(callback: types.CallbackQuery):
    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(text="Случайные отзывы", callback_data="random_reviews"),
            ]
        ]
    )
    logging.info(callback.message.from_user)
    (await callback.message.answer(f"Нажмите на кнопку 'случайные отзывы' что бы увидеть случайны отзыв!", reply_markup=kb))


@start_router.callback_query(F.data == "random_reviews")
async def random_reviews(callback: types.CallbackQuery):
    review1 = "Отличное приложение! Удобное управление и огромный выбор аниме."
    review2 = "Супер! Много крутых аниме, всегда что-то новое!"
    review3 = "Люблю этот сервис! Всегда находишь что-то интересное."
    review4 = "Отличное приложение для аниме! Рекомендую всем фанатам."
    review5 = "Супер! Удобное, быстрое и без лишних рекламных вставок."
    review6 = "Любимое приложение для просмотра аниме. Всегда под рукой!"
    review7 = "Очень удобное приложение, всегда актуальные новинки."
    review8 = "Отличное приложение для аниме, всегда все на высшем уровне."
    review9 = "Постоянно пользуюсь этим приложением! Всегда находишь что-то интересное."
    reviews = [review1, review2, review3, review4, review5, review6, review7, review8, review9]
    await callback.message.answer(random.choice(reviews))

