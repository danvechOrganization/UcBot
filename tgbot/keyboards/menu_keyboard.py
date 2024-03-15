from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup([
    [
        KeyboardButton(text="Активировать коды")
    ],
    [
        KeyboardButton(text="Пополнить коды"),
        KeyboardButton(text="Количество строк")
    ]
], resize_keyboard=True)