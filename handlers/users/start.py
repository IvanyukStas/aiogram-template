from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp
from utils.db_api.db_sqlite_functions import Aiosqlite_worker
from keyboards.inline.start import startup_kb


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Привет, {message.from_user.full_name}!\n"
                         f"Регестрируем вас в системе!",
                         reply_markup=startup_kb)
    db_worker = Aiosqlite_worker()
    await db_worker.add_new_user(message.from_user.full_name, message.from_user.id)

