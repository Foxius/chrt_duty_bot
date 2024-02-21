import telebot
import Database
from telebot import types

bot = telebot.TeleBot("7006292246:AAF7iWI7ayG60nhvXWS3ZQwwpFyUC5Ymu2I")
myId = 1594231051
historyGroupId = -4143701694


@bot.callback_query_handler(func=lambda call: True)
def answer(call):
    global rez, amount, group

    markup_inline = types.InlineKeyboardMarkup()



    try:


    except NameError as error:  # Ошибка перезапуска
        bot.send_message(call.message.chat.id,
                         text='Произошла ошибка из-за того что бот перезапускался, проставьте дежурства вручную или перезапустите меня командой /start')

    # Принимаем запрос TODO Ошибка перезапуска почему-то нет?
    if (len(call.data) == 18 or len(call.data) == 20):
        if len(call.data) == 18:
            good_person = int(call.data[:-9])
            bot.edit_message_text(chat_id=call.message.chat.id,
                                  message_id=call.message.message_id,
                                  text=f"Принято! Для {Database.get_who_am_i(good_person)[0][0]} БУДЕТ проставлено дежурство")
            Database.set_circles(good_person)
            bot.send_photo(good_person, 'https://i.ibb.co/6mYvDBN/kitajskie-memy-1.jpg',
                           caption='Парень Иван город Тверь молодец! Вам проставлено дежурство')
        elif len(call.data) == 20:
            good_person = int(call.data[:-10])
            bot.edit_message_text(chat_id=call.message.chat.id,
                                  message_id=call.message.message_id,
                                  text=f"Принято! Для {Database.get_who_am_i(good_person)[0][0]} БУДЕТ проставлено дежурство")
            Database.set_circles(good_person)
            bot.send_photo(good_person, 'https://i.ibb.co/6mYvDBN/kitajskie-memy-1.jpg',
                           caption='Парень Иван город Тверь молодец! Вам проставлено дежурство')

    # Отклоняем запрос
    if (len(call.data) == 27 or len(call.data) == 30):
        if len(call.data) == 27:
            bad_person = int(call.data[:-18])
            bot.edit_message_text(chat_id=call.message.chat.id,
                                  message_id=call.message.message_id,
                                  text=f"Принято! Для {Database.get_who_am_i(bad_person)[0][0]} НЕ будет поставлено дежурство.")
            bot.send_photo(bad_person, 'https://i.ibb.co/zFm3zvj/Powd-Vg9-X-t-A.jpg',
                           caption='О нет! Вы обмануть верховный лидер')
        elif len(call.data) == 30:
            bad_person = int(call.data[:-20])
            bot.edit_message_text(chat_id=call.message.chat.id,
                                  message_id=call.message.message_id,
                                  text=f"Принято! Для {Database.get_who_am_i(bad_person)[0][0]} НЕ будет поставлено дежурство.")
            bot.send_photo(bad_person, 'https://i.ibb.co/zFm3zvj/Powd-Vg9-X-t-A.jpg',
                           caption='О нет! Вы обмануть верховный лидер')


# TODO Сделать что если приоритет 2 отправлялось сообщение о том что по 2 кругу?
# TODO Можно: Дата последнего дежурства
