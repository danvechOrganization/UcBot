import sqlite3

import pyautogui
import pyperclip
from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import Message

from tgbot.misc import InputId
from tgbot.services.Counter.counter import Counter
from tgbot.services.Database.sqlite import Database


async def press_button(message: Message):
    photo = "tgbot/screenshots/Smena.png"
    try:
        photo_id = pyautogui.locateOnScreen(photo, confidence=0.8)
        pyautogui.sleep(2)
        pyautogui.click(photo_id)
        pyautogui.sleep(2)
        await message.answer("Введите ID")
        await InputId.Id.set()
    except:
        await message.answer("Не нашел изображение")


async def answer_id(message: Message, state: FSMContext):
    id = message.text
    await message.answer(f"Круто, ты ввел {id}")
    await state.finish()
    pyperclip.copy(id)

    pyautogui.click(940, 377)
    pyautogui.sleep(2)
    pyautogui.click(1131, 378)
    pyautogui.sleep(2)
    pyautogui.click(930, 375, button='right')
    pyautogui.sleep(2)
    pyautogui.click(1015, 526)
    pyautogui.sleep(2)
    pyautogui.click(952, 447)
    pyautogui.sleep(2)

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
                pyperclip.copy(code[0])
                pyautogui.click(864, 701)
                pyautogui.sleep(2)
                pyautogui.click(1070, 699)
                pyautogui.sleep(2)
                pyautogui.click(855, 700, button='right')
                pyautogui.sleep(2)
                pyautogui.click(889, 852)
                pyautogui.sleep(2)
                pyautogui.click(1195, 695)
                pyautogui.sleep(2)
                # Нажатие на Submit перед капчей
                pyautogui.click(945, 805)
                pyautogui.sleep(2)
                # Проверяем, есть ли на экране кнопка "Я не робот"
                try:
                    pyautogui.locateOnScreen('tgbot/screenshots/Captcha.png', confidence=0.9)
                    # Копируем аккаунт и пароль из базы данных
                    await copy_account_and_password(message, id)
                    Counter.add_counter()
                except pyautogui.ImageNotFoundException:
                    pyautogui.click(940, 425)
                    pyautogui.sleep(2)
                    # Активируем код
                    await message.answer(f'120 UC закинул на {id}')
                    db = Database("tgbot/services/Database/codes.db")
                    db.execute(f"UPDATE CODES SET IsUse = TRUE WHERE code = '{code[0]}'")
                    print(e)
                    break
        else:
            await message.answer("Коды закончились.")


async def copy_account_and_password(message: Message, id: str, photo: str):
    # Извлекаем следующий аккаунт и пароль из базы данных
    db = Database("tgbot/services/Database/codes.db")
    account_and_password = db.execute(
        f"SELECT login, pass FROM ACCOUNTS ORDER BY id ASC LIMIT 1 OFFSET {Counter.COUNTER}", fetchone=True)

    # Если аккаунт и пароль существуют, копируем их в буфер обмена
    if account_and_password:
        pyautogui.click(1186, 297)
        pyautogui.sleep(2)
        pyautogui.click(1475, 120)
        pyautogui.sleep(2)
        pyautogui.click(1395, 485)
        pyautogui.sleep(5)
        pyautogui.click(1480, 115)
        pyautogui.sleep(5)
        pyperclip.copy(account_and_password[0])
        pyautogui.click(930, 420, button='right')
        pyautogui.sleep(2)
        pyautogui.click(1008, 611)
        pyautogui.sleep(2)
        pyperclip.copy(account_and_password[1])
        pyautogui.click(952, 482, button='right')
        pyautogui.sleep(2)
        pyautogui.click(1029, 701)
        pyautogui.sleep(2)
        pyautogui.click(958, 589)
        pyautogui.sleep(6)
        smena_id = pyautogui.locateOnScreen(photo, confidence=0.9)
        pyautogui.sleep(2)
        pyautogui.click(smena_id)
        pyautogui.sleep(2)
        pyautogui.click(940, 377)
        pyautogui.sleep(2)
        pyautogui.click(1131, 378)
        pyautogui.sleep(2)
        pyperclip.copy(id)
        pyautogui.sleep(2)
        pyautogui.click(930, 375, button='right')
        pyautogui.sleep(2)
        pyautogui.click(963, 523)
        pyautogui.sleep(2)
        pyautogui.click(952, 447)
        pyautogui.sleep(2)
        await message.answer("Я сменил аккаунт")
    else:
        await message.answer("К сожалению, в базе данных нет аккаунтов и паролей.")


def register_120(dp: Dispatcher):
    dp.register_message_handler(press_button, text="120")
    dp.register_message_handler(answer_id, state=InputId.Id)
