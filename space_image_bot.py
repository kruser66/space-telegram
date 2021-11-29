import os
from dotenv import load_dotenv
from time import sleep
import telegram

IMAGES_DIR = 'images'


def push_images_to_telegram_channel(token, channel_id, delay):
    
    bot = telegram.Bot(token=token)

    for image in os.listdir(IMAGES_DIR):
        bot.send_document(chat_id=channel_id, document=open('images/{}'.format(image), 'rb'))
        print('Pushing image: {}'.format(image))
        sleep(delay)


if __name__ == '__main__':
    load_dotenv()
    TOKEN = os.getenv('BOT_TOKEN')
    CHANNEL_ID = os.getenv('CHANNEL_ID')
    DELAY = int(os.getenv('DELAY'))
    while True:
        push_images_to_telegram_channel(TOKEN, CHANNEL_ID, DELAY)
