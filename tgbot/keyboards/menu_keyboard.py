from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup([
    [
        KeyboardButton(text="Активировать коды")
    ],
    [
        KeyboardButton(text="Удалить Коды Исп."),
        KeyboardButton(text="Количество строк"),
        KeyboardButton(text="Запуск Браузера")
    ]
], resize_keyboard=True)