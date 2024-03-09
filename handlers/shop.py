from aiogram import Router, F, types
from aiogram.filters import Command
import logging
shop_router = Router()


@shop_router.message(Command("shop"))
async def about(message: types.Message):
    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(text="Товар №1", url="https://t.me"),
                types.InlineKeyboardButton(text="Товар №2", url="https://t.me"),
                types.InlineKeyboardButton(text="Товар №3", url="https://t.me"),
            ],
            [
                types.InlineKeyboardButton(text="Товар №4", url="https://t.me"),
                types.InlineKeyboardButton(text="Товар №5", url="https://t.me"),
                types.InlineKeyboardButton(text="Товар №6", url="https://t.me"),
            ],
            [
                types.InlineKeyboardButton(text="Товар №7", url="https://t.me"),
                types.InlineKeyboardButton(text="Товар №8", url="https://t.me"),
                types.InlineKeyboardButton(text="Товар №9", url="https://t.me"),
            ]

        ]
    )
    logging.info(message.from_user)
    (await message.answer(f"Наш магазин, {message.from_user.first_name}!", reply_markup=kb))