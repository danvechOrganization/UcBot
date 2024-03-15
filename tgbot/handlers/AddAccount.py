import os
import sqlite3

from aiogram import Dispatcher, types, Bot
from aiogram.types import Message

import pandas as pd


async def load_account(message: Message):
    # Проверяем, является ли документ Excel-файлом
    if message.document.mime_type == "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet":
        # Загружаем и читаем Excel-файл
        file_path = f"file_test.xlsx"
        await message.document.download(destination_file=file_path)
        df = pd.read_excel(file_path)

        # Если файл содержит коды, извлекаем их и добавляем в базу данных
        if "Коды" in df.columns:
            codes = df["Коды"].tolist()

            # Вставляем коды в базу данных
            conn = sqlite3.connect("tgbot/services/Database/codes.db")
            cursor = conn.cursor()
            for code in codes:
                cursor.execute("INSERT INTO CODES (code, IsUse) VALUES (?,?)", (code,False))
            conn.commit()
            cursor.close()
            conn.close()

            # Удаляем временный Excel-файл
            os.remove(file_path)

            # Отправляем сообщение пользователю
            await message.answer("Коды успешно пополнены. Спасибо!")

        # Если файл содержит аккаунты и пароли, извлекаем их и добавляем в базу данных
        elif "Аккаунт" in df.columns and "Пароль" in df.columns:
            accounts = df["Аккаунт"].tolist()
            passwords = df["Пароль"].tolist()

            # Вставляем аккаунты и пароли в базу данных
            conn = sqlite3.connect("tgbot/services/Database/codes.db")
            cursor = conn.cursor()
            for account, password in zip(accounts, passwords):
                cursor.execute("INSERT INTO accounts (account, password) VALUES (?, ?)", (account, password))
            conn.commit()
            cursor.close()
            conn.close()

            # Удаляем временный Excel-файл
            os.remove(file_path)

            # Отправляем сообщение пользователю
            await message.answer("Аккаунты успешно загружены. Спасибо!")
        else:
            await message.answer(
                "Присланный файл не содержит ни кодов, ни аккаунтов с паролями. Пожалуйста, пришли мне Excel-файл с нужными данными.")




def register_added_account(dp: Dispatcher):
    dp.register_message_handler(load_account, content_types=types.ContentType.DOCUMENT)
