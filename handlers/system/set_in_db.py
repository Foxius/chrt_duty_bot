from Database import cur, Database


def set_priority_plus_one(user_id):
    cur.execute(f"UPDATE users SET priority = priority + 1 WHERE userid = {user_id}")
    Database.commit()


def set_priority_to_zero():
    cur.execute("UPDATE users SET priority = 0 WHERE priority > 0")
    Database.commit()


def set_priority_to_zero_for_user(user_id):
    cur.execute(f"UPDATE users SET priority = 0 WHERE userid = {user_id}")
    Database.commit()


def set_priority_to_max(user_id):
    cur.execute(f"UPDATE users SET priority = priority + 9999 WHERE userid = {user_id}")
    Database.commit()


def set_priority_to_last():
    cur.execute(f"UPDATE users SET priority = priority - 9999 WHERE priority > 9998")
    Database.commit()


def set_circles(user_id):
    cur.execute(f"UPDATE users SET circles = circles + 1 WHERE userid = {user_id}")
    Database.commit()