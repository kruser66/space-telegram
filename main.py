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
API_KEY_NASA = 'ZC2fq55TIon3SurTcjBSMpgkoJmH067riPaPTpod'


def extarct_the_extension(url):
    return os.path.splitext(url.split('?')[0])[-1]


def download_images(image_url, image_name):
    print('Сохраняем картинку по ссылке {}'.format(image_url))
    filename = image_name.join(extarct_the_extension(image_url))
    response = requests.get(image_url)
    if response.ok:
        with open(os.path.join(IMAGES_DIR, filename), 'wb') as file:
            file.write(response.content)
        print('Картинка сохранена')


def fetch_spacex_last_launch():
    # ищем последний запуск
    response = requests.get('https://api.spacexdata.com/v3/launches/latest')

    # если нет последнего запуска, то выбираем случайным образом из предыдущих
    if not response.ok:
        response = requests.get('https://api.spacexdata.com/v3/launches/')
        if response.ok:
            last_start = response.json()[-1]['flight_number']
            response = requests.get('https://api.spacexdata.com/v3/launches/{}'.format(randint(1, last_start)))

    # загружаем картинки запуска (или последнего или случайного из предыдущих)
    if response.ok:
        images = response.json()['links']['flickr_images']
        for image_number, image in enumerate(images):
            download_images(image, 'spacex'.join(str(image_number + 1)))


def fetch_hubble_image(image_id):
    hubble_url = 'http://hubblesite.org/api/v3/image/{}'.format(str(image_id))
    response = requests.get(hubble_url)
    if response.ok:
        hubble_images = response.json()['image_files']
        images = [image['file_url'] for image in hubble_images]
        download_images(images[-1], 'hubble_' + str(image_id))


def fetch_nasa_apod():
    nasa_apod_url = 'https://api.nasa.gov/planetary/apod?api_key={}'.format(API_KEY_NASA)
    response = requests.get(nasa_apod_url)
    if response.ok:
        data = response.json()
        download_images(data['url'], 'nasa_apod_{}'.format(data['date']))


if __name__ == '__main__':
    # download_images('https://upload.wikimedia.org/wikipedia/commons/3/3f/HST-SM4.jpeg', 'habble')
    fetch_spacex_last_launch()
    # fetch_nasa_apod()
    # url = 'https://api.nasa.gov/EPIC/archive/natural/2021/11/20/png/epic_1b_20211120184615.png?api_key=ZC2fq55TIon3SurTcjBSMpgkoJmH067riPaPTpod'
    # print(extarct_the_extension(url))