import sqlite3

from aiogram import Dispatcher, Bot
from aiogram.types import Message

from tgbot import config


async def show_note(message: Message):
    # Подключаемся к базе данных
    conn = sqlite3.connect("tgbot/services/Database/codes.db")
    cursor = conn.cursor()
    # Выполняем запрос для получения количества строк
    cursor.execute("SELECT COUNT(*) FROM codes")
    # Получаем количество строк
    count_codes = cursor.fetchone()[0]

    # Выполняем запрос для получения количества строк в таблице codes_325
    cursor.execute("SELECT COUNT(*) FROM codes_325")
    # Получаем количество строк в таблице codes_325
    count_codes_325 = cursor.fetchone()[0]

    # Отправляем сообщение с количеством строк
    await message.answer(text=f"Кодов по 60: {count_codes}\n"
                               f"Кодов по 325: {count_codes_325}")
    # Закрываем соединение с базой данных
    cursor.close()
    conn.close()

def register_show_note(dp: Dispatcher):
    dp.register_message_handler(show_note, text="Количество строк")