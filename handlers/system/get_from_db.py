from Database import cur
from handlers.system.set_in_db import set_priority_plus_one


def get_choose_from_group(amount, group):  # TODO костыль?
    cur.execute(
        f"SELECT * FROM users WHERE in_group = {group} ORDER BY priority, circles LIMIT {amount}")
    pretender = cur.fetchall()

    for i in range(len(pretender)):
        if pretender[i][5] != 0:
            cur.execute(
                f"SELECT * FROM users WHERE in_group = {group} AND priorityDuty = {pretender[i][5]} AND priority = {pretender[i][2]} ORDER BY circles LIMIT {amount}")
            two_pretenders = cur.fetchall()
            if len(two_pretenders) < 2:
                set_priority_plus_one(two_pretenders[0][0])  # TODO : Bug when another group his member / NoneFix mb
                return get_choose_from_group(amount, group)
            else:
                amount -= 2
                two_pretenders.extend(get_choose_from_group(amount, group))  # TODO: Rename
                return two_pretenders
    return pretender


def get_choose_from_all(amount):
    cur.execute(f"SELECT * FROM users ORDER BY priority, circles LIMIT {amount}")
    pretender = cur.fetchall()

    for i in range(len(pretender)):
        if pretender[i][5] != 0:
            cur.execute(
                f"SELECT * FROM users WHERE priorityDuty = {pretender[i][5]} AND priority = {pretender[i][2]} ORDER BY circles LIMIT {amount}")
            two_pretenders = cur.fetchall()
            if len(two_pretenders) < 2:
                set_priority_plus_one(two_pretenders[0][0])  # TODO : Bug when another group his member / NoneFix mb
                return get_choose_from_all(amount)
            else:
                amount -= 2
                two_pretenders.extend(get_choose_from_all(amount))  # TODO: Rename
                return two_pretenders
    return pretender


def get_who_am_i(user_id):
    cur.execute(f"SELECT name, circles, in_group FROM users WHERE userid = ?", (int(user_id),))
    who = cur.fetchall()
    if who:
        return who
    else:
        raise Exception("Человека нет в базе данных")


def get_priority_duty():
    cur.execute("SELECT priorityDuty FROM users ")


def get_rate():
    cur.execute("SELECT name, circles FROM users ORDER BY circles DESC")
    rate = cur.fetchall()
    return rate
