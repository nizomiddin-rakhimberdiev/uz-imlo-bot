"""
This is a echo bot.
It echoes any incoming text messages.
"""

import logging
from aiogram import Bot, Dispatcher, executor, types

from checkWord import checkWords

API_TOKEN = '5470513250:AAG3fBz-yCWmoYNEVutHNdj_i-cD67STe7A'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("uz_imlo Botiga xush kelibsiz!")


@dp.message_handler(commands=['help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Botdan faydalanish uchun so'z yuboring!")


@dp.message_handler()
async def checkImlo(message: types.Message):
    word = message.text
    result = checkWords(word)

    if result['available']:
        response = f"✅ {word.capitalize()}\n"
    else:
        response = f"❌ {word.capitalize()}\n"
        for text in result['matches']:
            response += f"✅ {text.capitalize()}\n"
    await message.answer(response)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
