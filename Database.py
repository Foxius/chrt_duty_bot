import sqlite3

Database = sqlite3.connect('users.db', check_same_thread=False)
cur = Database.cursor()
#
# cur.execute("""CREATE TABLE IF NOT EXISTS users(
#    userid INT PRIMARY KEY,
#    circles INT,
#    priority INT,
#    in_group INT,
#    name TEXT,
#    priorityDuty);
# """)
# Database.commit()




