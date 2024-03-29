import sqlite3


from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import Message

from tgbot.misc import InputId_120
from tgbot.pars.id import id_call
from tgbot.pars.insert_code import code_call
from tgbot.services.Database.sqlite import Database

async def press_button_120(message: Message):
    await message.answer("Введите ID")
    await InputId_120.Id.set()


async def answer_id_120(message: Message, state: FSMContext):
    id = message.text
    await message.answer(f"Круто, ты ввел {id}")
    await state.finish()
    await id_call(id)

    for i in range(2):
        while True:
            # Извлекаем первый код из базы данных
            conn = sqlite3.connect("tgbot/services/Database/codes.db")
            cursor = conn.cursor()
            cursor.execute("SELECT code FROM CODES WHERE IsUse = False LIMIT 1")
            code = cursor.fetchone()
            conn.commit()
            cursor.close()
            conn.close()

            # Если код существует, копируем его и удаляем из базы данных
            if code:
                code = code[0]
                success = await code_call(code, id)
                if success:
                    await message.answer("Авторизовался, вновь ввожу код!")
                    continue
                else:
                    db = Database("tgbot/services/Database/codes.db")
                    db.execute(f"UPDATE CODES SET IsUse = TRUE WHERE code = '{code}'")
                    break
            else:
                await message.answer("Коды закончились.")
    await message.answer(f'120 UC закинул на {id}')


def register_120(dp: Dispatcher):
    dp.register_message_handler(press_button_120, text='120')
    dp.register_message_handler(answer_id_120, state=InputId_120.Id)
