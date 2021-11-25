import telegram

TOKEN = '2119927034:AAH67gluVcV1K3wgYC6jVLeaO88Pmyfe0w0'

bot = telegram.Bot(token=TOKEN)

print(bot.get_me())

updates = bot.get_updates()
print(updates[0])

bot.send_message(chat_id='@spaceimages_new', text="Первый пост Бота в канал")