import pyautogui
import pyperclip
from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import Message

from tgbot.misc import InputId

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

    pyautogui.moveTo(1042 + (1042 * 0.2) , 414 + (414 * 0.2))
    x,y = pyautogui.position()
    print(x, y)
    pyautogui.sleep(10)
    pyautogui.click(1430, 614)
    pyautogui.sleep(2)

    pyperclip.copy(id)
    pyautogui.sleep(2)
    pyautogui.click(1242, 614, button='right')
    pyautogui.sleep(2)
    pyautogui.click(1209, 762)
    pyautogui.sleep(2)
    pyautogui.click(1242, 707)
    pyautogui.sleep(2)

def register_60(dp: Dispatcher):
    dp.register_message_handler(press_button, text="60")
    dp.register_message_handler(answer_id, state=InputId.Id)