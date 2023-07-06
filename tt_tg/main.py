from aiogram import types, Bot, Dispatcher
from aiogram.utils import executor
from decouple import

TOKEN = ""

bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await bot.send_message(message.from_user.id, f"Привет хозяин {message.from_user.full_name}!")
    await message.answer("This is an answer method!")
    await message.reply("This is a reply method!")


@dp.message_handler()
async def echo(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id, text=message.text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
