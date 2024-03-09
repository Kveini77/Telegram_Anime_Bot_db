from aiogram import Router, F, types
from aiogram.filters import Command
import logging
import random
reviews_router = Router()


@reviews_router.message(Command("reviews"))
async def about(message: types.Message):
    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(text="Случайные отзывы", callback_data="reviews"),
            ]
        ]
    )
    logging.info(message.from_user)
    (await message.answer(f"Нажмите на кнопку 'случайные отзывы' что бы увидеть случайны отзыв!", reply_markup=kb))


@reviews_router.callback_query(F.data == "reviews")
async def about(callback: types.CallbackQuery):
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

