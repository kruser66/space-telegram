import os
from dotenv import load_dotenv
from time import sleep
import telegram

IMAGES_DIR = 'images'
DELAY = 30  # in seconds


def push_images_to_telegram_channel(token, channel_id, delay):
    bot = telegram.Bot(token=token)

    for image in os.listdir(IMAGES_DIR):
        bot.send_document(chat_id=channel_id, document=open('images/{}'.format(image), 'rb'))
        print('Pushing image: {}'.format(image))
        sleep(delay)


def main():
    load_dotenv()
    token = os.getenv('BOT_TOKEN')
    channel_id = os.getenv('CHANNEL_ID')
    while True:
        push_images_to_telegram_channel(token, channel_id, DELAY)


if __name__ == '__main__':
    main()
