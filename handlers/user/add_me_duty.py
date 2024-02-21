from loader import bot
from handlers.system.get_from_db import get_who_am_i
from telebot import types
from data.config import historyGroupId, admin_username


@bot.message_handler(func=lambda message: message.text == "Поставить мне дежурство")
def add_me_duty(message):
    person = get_who_am_i(message.from_user.id)
    markup = types.InlineKeyboardMarkup()
    bot.send_message(message.chat.id,
                     f"Вам будет добавлено дежурство, когда {admin_username} это подтвердят.")

    item_accept = types.InlineKeyboardButton(text="Поставить", callback_data=f"add_yes_{message.from_user.id}")
    item_decline = types.InlineKeyboardButton(text="Отклонить", callback_data=f"add_no_{message.from_user.id}")

    markup.add(item_accept, item_decline)

    bot.send_message(historyGroupId,
                     f"{person[0][0]} хочет чтобы ему поставили дежурство.",
                     reply_markup=markup)
