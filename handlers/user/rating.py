from loader import bot
from handlers.system.get_from_db import get_rate


@bot.message_handler(func=lambda message: message.text == "Рейтинг дежурств")
def rating(message):
    rate = get_rate()
    text = ''
    for i in range(27):
        text += f"{rate[i][0]} - {rate[i][1]}\n"
    bot.send_message(message.chat.id,
                     f"{text}")