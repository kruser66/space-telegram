import requests
import os
from random import randint
# from dotenv import load_dotenv
# from instabot import Bot
# import random
# import glob

IMAGES_DIR = 'images'
if not os.path.exists(IMAGES_DIR):
    os.makedirs(IMAGES_DIR)


def download_images(image_url, image_name):
    print('Сохраняем картинку по ссылке {}'.format(image_url))
    filename = image_name + os.path.splitext(image_url.split('?')[0])[-1]
    response = requests.get(image_url)
    if response.ok:
        with open(os.path.join(IMAGES_DIR, filename), 'wb') as file:
            file.write(response.content)
        print('Картинка сохранена')


def fetch_spacex_last_launch():
    # ищем последний запуск
    response = requests.get('https://api.spacexdata.com/v3/launches/latest')

    # если нет последнего, выбираем случайным образом из предыдущих
    if not response.ok:
        response = requests.get('https://api.spacexdata.com/v3/launches/')
        if response.ok:
            last_start = response.json()[-1]['flight_number']
            response = requests.get('https://api.spacexdata.com/v3/launches/{}'.format(randint(1, last_start)))

    # загружаем картинки запуска (или последнего или случайного из предыдущих)
    if response.ok:
        images = response.json()['links']['flickr_images']
        for image_number, image in enumerate(images):
            download_images(image, 'spacex' + str(image_number + 1))


def fetch_hubble_image(image_id):
    hubble_url = 'http://hubblesite.org/api/v3/image/' + str(image_id)
    response = requests.get(hubble_url)
    if response.ok:
        hubble_images = response.json()['image_files']
        images = [image['file_url'] for image in hubble_images]
        download_images(images[-1], 'hubble_' + str(image_id))


if __name__ == '__main__':
    # download_images('https://upload.wikimedia.org/wikipedia/commons/3/3f/HST-SM4.jpeg', 'habble')
    fetch_spacex_last_launch()