from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

codes = ReplyKeyboardMarkup([
    [
        KeyboardButton(text="60"),
        KeyboardButton(text="120"),
        KeyboardButton(text="180")
    ],
    [
        KeyboardButton(text="🔙")
    ]
], resize_keyboard=True)