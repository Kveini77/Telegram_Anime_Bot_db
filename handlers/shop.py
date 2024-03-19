from aiogram import Router, F, types
import logging
from handlers.start import start_router
from bot import bot, dp, db

shop_router = Router()


@start_router.callback_query(F.data == "shop")
async def shop(callback: types.CallbackQuery):
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
    products = db.get_all_product()
    products_text = "\n".join([f"Название: {product[0]}, Цена: {product[1]}" for product in products])

    logging.info(callback.message.from_user)
    (await callback.message.answer_photo(types.FSInputFile("images/shop.jpg"), caption=f"Напиш продукты:\n{products_text}", reply_markup=kb))