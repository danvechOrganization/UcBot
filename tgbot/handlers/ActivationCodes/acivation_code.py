from aiogram import Dispatcher
from aiogram.types import Message

from tgbot.keyboards import codes, menu


async def show_code(message: Message):
    await message.answer("Выберите код", reply_markup=codes)

async def back_menu(message:Message):
    await message.answer("Вернуть меню", reply_markup=menu)


def register_activation_code(dp: Dispatcher):
    dp.register_message_handler(show_code, text="Активировать коды")
    dp.register_message_handler(back_menu, text="🔙")