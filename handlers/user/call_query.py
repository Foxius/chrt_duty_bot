from telebot import types

import data.config
from handlers.system.set_in_db import set_priority_plus_one, set_priority_to_zero, set_circles
from loader import bot
from handlers.system.other import send_list_of_duty
from handlers.system.get_from_db import get_choose_from_group, get_choose_from_all, get_who_am_i


@bot.callback_query_handler(func=lambda call: call.data.startswith("group_"))
def callback_duty_amount(call):
    group = call.data.split("_")[1]
    amount = call.data.split("_")[2]
    if group == "lonely":
        group = 0
        rez = get_choose_from_all(amount)
        data.config.rez = rez

    else:
        rez = get_choose_from_group(amount, group)
        data.config.rez = rez

    send_list_of_duty(call, int(amount), rez, group)


@bot.callback_query_handler(func=lambda call: call.data.startswith("busy_"))
def callback_busy(call):
    who_cant_duty = call.data.split("_")[1]
    group = call.data.split("_")[2]
    amount = call.data.split("_")[3]
    set_priority_plus_one(who_cant_duty)
    bot.edit_message_text(text="Подберём других...", chat_id=call.message.chat.id,
                          message_id=call.message.message_id)
    if group == "0":
        rez = get_choose_from_all(amount)
        data.config.rez = rez
        send_list_of_duty(call, amount, rez, group)
    else:
        rez = get_choose_from_group(amount, group)
        data.config.rez = rez
        send_list_of_duty(call, amount, rez, group)


@bot.callback_query_handler(func=lambda call: call.data.startswith("accept_duty_list_"))
def callback_accept_duty_list(call):
    markup_inline = types.InlineKeyboardMarkup()
    group = call.data.split("_")[4]
    names = data.config.names
    amount = call.data.split("_")[5]
    data.config.amount = amount

    if group == 0:
        item_reject_list_lonely = types.InlineKeyboardButton(text="Назад", callback_data="group_lonely")
        markup_inline.add(item_reject_list_lonely)

    else:
        item_reject_list_group = types.InlineKeyboardButton(text="Назад", callback_data=f"group_{str(group)}")
        markup_inline.add(item_reject_list_group)

    item_accept = types.InlineKeyboardButton(text="Подтвердить", callback_data="accept")
    markup_inline.add(item_accept)

    bot.send_message(call.message.chat.id,
                     f"Нажми на кнопку 'Подтвердить', когда {names} отдежурят",
                     reply_markup=markup_inline)


@bot.callback_query_handler(func=lambda call: call.data == "accept")
def callback_accept(call):
    set_priority_to_zero()
    amount = data.config.amount
    print(data.config.rez)
    bot.send_message(data.config.historyGroupId,
                     text=f'{get_who_am_i(call.message.chat.id)[0][0]} поставил дежурства для: {data.config.names}')
    for i in range(int(amount)):
        set_circles(data.config.rez[i][0])
    bot.edit_message_text(chat_id=call.message.chat.id,
                          message_id=call.message.message_id,
                          text="Принято!")
    bot.send_message(call.message.chat.id, text="Дежурства проставлены. Спасибо!")


@bot.callback_query_handler(func=lambda call: call.data.startswith("add_"))
def callback_add(call):
    choice = call.data.split("_")[1]
    user = call.data.split("_")[2]

    if choice == "yes":
        bot.edit_message_text(chat_id=call.message.chat.id,
                              message_id=call.message.message_id,
                              text=f"Принято! Для {get_who_am_i(user)[0][0]} БУДЕТ проставлено дежурство")
        set_circles(user)
        bot.send_photo(user, 'https://i.ibb.co/6mYvDBN/kitajskie-memy-1.jpg',
                       caption='Парень Иван город Тверь молодец! Вам проставлено дежурство')
    else:
        bot.edit_message_text(chat_id=call.message.chat.id,
                              message_id=call.message.message_id,
                              text=f"Принято! Для {get_who_am_i(user)[0][0]} НЕ будет поставлено дежурство.")
        bot.send_photo(user, 'https://i.ibb.co/zFm3zvj/Powd-Vg9-X-t-A.jpg',
                       caption='О нет! Вы обмануть верховный лидер')

@bot.callback_query_handler(func=lambda call: int(call.data) in range(7))
def callback_duty_amount(call):
    markup = types.InlineKeyboardMarkup()
    amount = call.data
    item_first = types.InlineKeyboardButton(text="Первая", callback_data=f"group_1_{amount}")
    item_second = types.InlineKeyboardButton(text="Вторая", callback_data=f"group_2_{amount}")
    item_lonely = types.InlineKeyboardButton(text="Нет", callback_data=f"group_lonely_{amount}")
    markup.add(item_first, item_second, item_lonely)

    bot.send_message(call.message.chat.id,
                     "Самый лучший\n Нужна определённая группа?",
                     reply_markup=markup)
