from loader import bot
from handlers.user import start, profile, rating, assign_duty, call_query, add_me_duty


bot.polling(none_stop=True, timeout=666)