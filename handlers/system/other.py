from loader import bot
from telebot import types
import data.config as config


def send_list_of_duty(call, amount, rez, group):
    markup = types.InlineKeyboardMarkup()
    for i in range(amount):
        config.names += rez[i][4] + " "
        item_cant = types.InlineKeyboardButton(text=f"{rez[i][4]} занят", callback_data=f"busy_{rez[i][0]}_{group}_{amount}")
        markup.add(item_cant)

    item_accept_list = types.InlineKeyboardButton(text="Готово", callback_data=f"accept_duty_list_{rez[i][0]}_{group}_{amount}")
    markup.add(item_accept_list)

    bot.send_message(call.message.chat.id, f"Дежурные/й - {config.names}", reply_markup=markup)
