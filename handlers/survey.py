from aiogram import Router, F, types
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
import logging
survey_router = Router()


class Survey(StatesGroup):
    name = State()
    gender = State()
    age = State()
    genre = State()
    episodes = State()
    favorite_director = State()
    card_number = State()


@survey_router.callback_query(F.data == "survey")
async def survey(callback: types.CallbackQuery):
    kb = types.ReplyKeyboardMarkup(
                keyboard=[
                    [types.KeyboardButton(text="Точно пройти опрос")]
                ]
            )
    await callback.message.answer("Вы точно хотите пройти опрос?", reply_markup=kb)


@survey_router.message(F.text.lower() == "точно пройти опрос")
async def start_survey(message: types.message, state: FSMContext):
    await state.set_state(Survey.name)
    await message.answer("Как вас зовут?")


@survey_router.message(Survey.name)
async def process_name(message: types.message, state: FSMContext):
    kb = types.ReplyKeyboardMarkup(
        keyboard=[
            [types.KeyboardButton(text="Мужской")],
            [types.KeyboardButton(text="Женский")],
            [types.KeyboardButton(text="Холикоптер")]
        ]
    )
    name = message.text
    await state.set_state(Survey.gender)
    await message.answer("Какой ваш пол?", reply_markup=kb)


@survey_router.message(Survey.gender)
async def process_name(message: types.message, state: FSMContext):
    gender = message.text
    if gender.lower() not in ["мужской", "женский", "холикоптер"]:
        await message.answer("Вы можете ввести только один из трех гендеров 'Мужской, Женский, Холикоптер'")
        return
    logging.info(gender)
    await state.set_state(Survey.age)
    await message.answer("Какой ваш возраст?")


@survey_router.message(Survey.age)
async def process_name(message: types.message, state: FSMContext):
    age = message.text
    if not age.isdigit():
        await message.answer("Возраст должен быть в виде числа")
        return
    elif int(age) < 6 or (int(age) > 100):
        await message.answer("Возраст не меньше 6 и не больше 100")
        return
    await state.set_state(Survey.genre)
    await message.answer("Ваш любимый жанр?")


@survey_router.message(Survey.genre)
async def process_name(message: types.message, state: FSMContext):
    kb = types.ReplyKeyboardMarkup(
        keyboard=[
            [types.KeyboardButton(text="12 серий")],
            [types.KeyboardButton(text="24 серий")],
            [types.KeyboardButton(text=">12 серий")]
        ]
    )
    genre = message.text
    await state.set_state(Survey.episodes)
    await message.answer("Сколько вам эпизодов нравится?", reply_markup=kb)


@survey_router.message(Survey.episodes)
async def process_name(message: types.message, state: FSMContext):
    episodes = message.text
    await state.set_state(Survey.favorite_director)
    await message.answer("Кто ваш любимый режисер?")


@survey_router.message(Survey.favorite_director)
async def process_name(message: types.message, state: FSMContext):
    favorite_director = message.text
    await state.set_state(Survey.card_number)
    await message.answer("И номер вашей кредитной карты пж")


@survey_router.message(Survey.card_number)
async def process_name(message: types.message):
    card_number = message.text
    card_number_without_spaces = card_number.replace(' ', '')
    if not card_number_without_spaces.isdigit():
        await message.answer("Вы должны ввести номер карты в формате '**** **** **** ****'")
        return
    elif not len(card_number_without_spaces) == 16:
        await message.answer("Вы должны ввести номер карты из 16 цифр в формате '**** **** **** ****'")
        return
    await message.answer("спс за карточку броу")
