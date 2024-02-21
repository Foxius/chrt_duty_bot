from loader import bot
from telebot import types
from data.config import admin_username
from handlers.system.get_from_db import get_who_am_i


@bot.message_handler(commands=["start"])
def start(message):
    try:
        get_who_am_i(message.chat.id)[0][1]

        markup_reply = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

        item_duty = types.KeyboardButton("Назначить дежурных")
        item_rate = types.KeyboardButton("Рейтинг дежурств")
        item_profile = types.KeyboardButton("Мой профиль")
        item_duty_add = types.KeyboardButton("Поставить мне дежурство")

        markup_reply.add(item_duty_add, item_rate, item_profile, item_duty)

        bot.send_message(message.chat.id,
                         f"Привет! Этого бота разработал {admin_username}\n\nТы можешь спокойно распространять бота в том или ином виде, но с указанием моего авторства)",
                         reply_markup=markup_reply)
    except Exception as e:
        print(e)
        bot.send_message(message.chat.id,
                         f"Вас нет в списке бота, если произошла ужасная ошибка, Вы можете написать мне {admin_username}")
        print(message.chat.id)
