from aiogram import Router, types
from aiogram.filters import Command
import random
from os import path
import os

pic_router = Router()


@pic_router.message(Command("random_pic"))
async def send_random_pic(message: types.Message):
    photos = os.listdir("images")
    random_photos = random.choice(photos)
    photos_path = path.join("images", random_photos)
    file = types.FSInputFile(photos_path)
    await message.answer_photo(file, caption="Котик")