from aiogram import Bot, Dispatcher, executor, types
import logging


BOT_TOKEN = '5855245938:AAGtjxuqlVYnpkgifeJ-vcuIcgwAbl4v-Xc'
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
def start(messege):
    mess = f"Привет мой создатель, {messege.from_user.first_name} "
    bot.send_message(messege.chat.id, mess, parse_mode="html")

@dp.message_handler(commands=["website"])
def website(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton(f"перейти на сайт", url="https://www.youtube.com/watch?v=btKpU3lODn4"))
    bot.send_message(message.chat.id, "перейти на сайт", reply_markup=markup)


@dp.message_handler(content_types=["text"])
def get_user_text(message):
    if message.text == "Привет":
        bot.send_message(message.chat.id, f"Пока")

    elif message.text == "как дела?":
        bot.send_message(message.chat.id, f"плохо((")

    elif message.text == "что делаешь?":
        bot.send_message(message.chat.id, f"Лежу, и вообще отстань от меня")

    elif message.text == "Ты что не стой ноги встал":
        bot.send_message(message.chat.id, f"Очень смешно, все пока!!!")

    elif message.text == "Какая сегодня погода?":
        bot.send_message(message.chat.id, f"Вроде нормально))")

    else:
        bot.send_message(message.chat.id, f"Я тебя не понимаю")



bot.polling(none_stop=True)

