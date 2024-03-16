import sqlite3

from aiogram import Dispatcher
from aiogram.types import Message
from tgbot.services.Database.sqlite import Database


async def del_true(message: Message):
    db = Database("tgbot/services/Database/codes.db")
    db.delete_codes()
    conn = sqlite3.connect("tgbot/services/Database/codes.db")
    cursor = conn.cursor()
    # Выполняем запрос для получения количества строк
    cursor.execute("SELECT COUNT(*) FROM codes")
    # Получаем количество строк
    count = cursor.fetchone()[0]
    # Отправляем сообщение с количеством строк
    await message.answer(text=f"Я удалил использованные. В базе осталось: {count}")
    # Закрываем соединение с базой данных
    cursor.close()
    conn.close()


def register_del_true(dp: Dispatcher):
    dp.register_message_handler(del_true, text="Удалить Коды Исп.")