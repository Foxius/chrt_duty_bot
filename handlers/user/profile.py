from loader import bot
from handlers.system.get_from_db import get_who_am_i


@bot.message_handler(func=lambda message: message.text == "Мой профиль")
def profile(message):
    person = get_who_am_i(message.from_user.id)
    bot.send_message(message.chat.id,
                     f"Вы - {person[0][0]} \n\nКоличество ваших дежурств - {person[0][1]} \n\nВаша группа - {person[0][2]}")
