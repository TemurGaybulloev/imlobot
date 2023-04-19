import logging
from checking import CheckWord
from transliterate import transliterate
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '6252327819:AAFgUZ1B5ZvHNPGsb99Rhg9BweT2fjmo6CA'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")



@dp.message_handler()
async def Tekshirish(message: types.Message):
    # old style:
    # await bot.send_message(message.chat.id, message.text)
    matn = message.text.split()
    for message.text in matn:
        tarjima = transliterate(message.text, 'cyrillic')
        if message.text == tarjima:
            javob = CheckWord(message.text)
            if javob['Available']:
                await message.answer(f"{javob['Available']} => {message.text.capitalize()}")
            else:
                match = list(javob['matches'])
                matchlar = "\n".join(match)
        else:
            javob = CheckWord(tarjima)
            if javob['Available']:
                await message.answer(f"{javob['Available']} => {message.text.capitalize()}")
            else:
                match = list(javob['matches'])
                matchlar = "\n".join(match)
                oxiri = f"{javob['Available']} => {message.text.capitalize()}\nThis options maybe true:\n{matchlar}"
                song = transliterate(oxiri, 'latin')
                await message.answer(song)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)