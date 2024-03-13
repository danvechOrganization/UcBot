from aiogram import Dispatcher
from aiogram.types import Message

from tgbot.keyboards import codes

async def show_code(message: Message):
    await message.answer("Выберите код", reply_markup=codes)


def register_activation_code(dp: Dispatcher):
    dp.register_message_handler(show_code, text="Активировать коды")