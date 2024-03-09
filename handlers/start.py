from aiogram import Router, F, types
from aiogram.filters import Command
import logging


start_router = Router()


@start_router.message(Command("start"))
async def start(message: types.Message):
    kb =types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(text="Моя информация", url="https://telegra.ph")
            ],
            [
                types.InlineKeyboardButton(text="Моя информациzя", url="https://telegra.ph"),
                types.InlineKeyboardButton(text="Моя информациzzя", url="https://telegra.ph")
            ],
            [
                types.InlineKeyboardButton(text="О нас", callback_data="about")
            ],
            [
                types.InlineKeyboardButton(text="сделать заказ",
                                           callback_data="make_order")
            ]
        ]
    )
    logging.info(message.from_user)
    (await message.answer(f"Привет, {message.from_user.first_name}!", reply_markup=kb))


@start_router.callback_query(F.data == "about")
async def about(callback: types.CallbackQuery):
    await callback.message.answer("О нас")


@start_router.callback_query(F.data == "make_order")
async def about(callback: types.CallbackQuery):
    await callback.message.answer("О нас")