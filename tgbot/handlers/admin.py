import os.path

from aiogram import Dispatcher
from aiogram.types import Message

from tgbot.keyboards.menu_keyboard import menu
from tgbot.services.Database.sqlite import Database


async def admin_start(message: Message):
    path_to_db = "tgbot/services/Database/codes.db"
    if(os.path.isfile(path_to_db)):
        await message.answer("База данных уже создана.\n Приветствую администратор")
    else:
        db = Database("tgbot/services/Database/codes.db")
        db.create_table()
        await message.answer("Создание базы данных прошло успешно")

async def show_menu(message: Message):
    await message.answer("Выберите действие" ,reply_markup=menu)


def register_admin(dp: Dispatcher):
    dp.register_message_handler(admin_start, commands=["start"], state="*", is_admin=True)
    dp.register_message_handler(show_menu, commands=["menu"], is_admin=True)
