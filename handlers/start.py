from aiogram import Router, F, types
from aiogram.filters import Command
import logging

from keyboards.all_keyboards import start_kb

start_router = Router()


@start_router.message(Command("start"))
async def start(message: types.Message):
    logging.info(message.from_user)
    (await message.answer_photo(types.FSInputFile("images/anixart.png"), caption=f"Здравствуйте, {message.from_user.first_name}!", reply_markup=start_kb()))


@start_router.callback_query(F.data == "contacts")
async def contacts(callback: types.CallbackQuery):
    await callback.message.answer("Название приложения: Anixart\n"
                                  "Email поддержки: support@.com\n"
                                  "Телефон поддержки: +1-800-ANIME-APP\n"
                                  "Адрес офиса: 1234 Аниме улица, Город, Страна, Почтовый индекс\n"
                                  "Официальный сайт: https://\n\n"
                                  "Группа в социальных сетях:\n"
                                  "ВКонтакте: https://vk.com/\n"
                                  "Instagram: https://instagram.com/\n"
                                  "Facebook: https://facebook.com/")


@start_router.callback_query(F.data == "about")
async def about(callback: types.CallbackQuery):
    await callback.message.answer("Anixart - это ваш путеводитель в мир японской анимации! Мы стараемся делать просмотр аниме максимально удобным, интересным и доступным для всех любителей этого жанра.\n\n"
                                  "Наше приложение предлагает огромный выбор аниме различных жанров - от классики до современных хитов. Мы постоянно обновляем наш каталог, чтобы вы всегда могли наслаждаться свежими релизами и старыми любимцами.\n\n"
                                  "Наши цели - это создание уютного места для всех, кто ценит аниме. Мы стремимся к тому, чтобы каждый наш пользователь получал максимум удовольствия от просмотра и находил новые аниме, которые полюбит.\n\n")


