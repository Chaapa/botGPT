from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

from chatGPT import openAI, BOT_PERSONALITY
from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Привет!\nНапиши мне что-нибудь!")


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply("Пиши всё что угодно и тебе ответит ботик)")


@dp.message_handler()
async def talking_bot(msg: types.Message):
    if msg.text:
        await bot.send_message(msg.from_user.id, openAI(f'{BOT_PERSONALITY}{msg.text}'))
    else:
        await bot.send_message(msg.from_user.id, 'НЕ НУЖНО ОТПРАВЛЯТЬ ПУСТЫЕ СООБЩЕНИЯ!!!')


if __name__ == '__main__':
    executor.start_polling(dp)
