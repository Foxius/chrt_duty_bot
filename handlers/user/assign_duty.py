from telebot import types
from loader import bot


@bot.message_handler(func=lambda message: message.text == "Назначить дежурных")
def assign_duty(message):
    markup = types.InlineKeyboardMarkup()
    for i in range(1, 7):
        btn = types.InlineKeyboardButton(text=i, callback_data=i)
        markup.add(btn)

    bot.send_message(message.chat.id,
                     "Сколько дежурных нужно?",
                     reply_markup=markup)
    