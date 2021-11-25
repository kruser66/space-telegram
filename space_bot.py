import telegram
from main import *


TOKEN = os.getenv('BOT_TOKEN')

bot = telegram.Bot(token=TOKEN)

# bot.send_message(chat_id='@spaceimages_new', text="Первый пост Бота в канал")
bot.send_document(chat_id='@spaceimages_new', document=open('images/1.jpg', 'rb'))