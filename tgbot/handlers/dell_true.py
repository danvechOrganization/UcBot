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
    count_codes = cursor.fetchone()[0]
    # Выполняем запрос для получения количества строк в таблице codes_325
    cursor.execute("SELECT COUNT(*) FROM codes_325")
    # Получаем количество строк
    count_codes_325 = cursor.fetchone()[0]
    # Отправляем сообщение с количеством строк
    await message.answer(text=f"Я удалил использованные,60 осталось: {count_codes}\n"
                               f"Я удалил использованные,325 осталось: {count_codes_325}")
    # Закрываем соединение с базой данных
    cursor.close()
    conn.close()


def register_del_true(dp: Dispatcher):
    dp.register_message_handler(del_true, text="Удалить Коды Исп.")