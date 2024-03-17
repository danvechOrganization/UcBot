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
    count = cursor.fetchone()[0]
    # Отправляем сообщение с количеством строк
    await message.answer(text=f"Количество строк в базе данных: {count}")
    # Закрываем соединение с базой данных
    cursor.close()
    conn.close()

def register_show_note(dp: Dispatcher):
    dp.register_message_handler(show_note, text="Количество строк")