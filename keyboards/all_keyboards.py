from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton


def start_kb():
    kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="Контакты", callback_data="contacts"),
                InlineKeyboardButton(text="О нас", callback_data="about")
            ],
            [
                InlineKeyboardButton(text="Магазин", callback_data="shop"),
                InlineKeyboardButton(text="Отзывы", callback_data="reviews")
            ],
            [
                InlineKeyboardButton(text="Пройти опрос", callback_data="survey")
            ]

        ]
    )
    return kb



