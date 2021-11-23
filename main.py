import requests
import os
from random import randint
from datetime import datetime
from dotenv import load_dotenv


IMAGES_DIR = 'images'
if not os.path.exists(IMAGES_DIR):
    os.makedirs(IMAGES_DIR)
load_dotenv()
NASA_API_KEY = os.getenv('NASA_API_KEY')


def extarct_the_extension(url):
    return os.path.splitext(url.split('?')[0])[-1]


def download_images(image_url, image_name):
    print('Сохраняем картинку по ссылке {}'.format(image_url.split('?')[0]))
    filename = f'{image_name}{extarct_the_extension(image_url)}'
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


def fetch_nasa_apod(count):
    nasa_apod_url = 'https://api.nasa.gov/planetary/apod'
    params = {
        'api_key': NASA_API_KEY,
        'count': count,
    }
    response = requests.get(nasa_apod_url, params=params)
    if response.ok:
        nasa_apod_images = response.json()
        for data in nasa_apod_images:
            download_images(data['hdurl'], 'nasa_apod_{}'.format(data['date']))


def fetch_nasa_epic(count=5):
    nasa_epic_url = 'https://api.nasa.gov/EPIC/api/natural'
    params = {
        'api_key': NASA_API_KEY,
    }
    response = requests.get(nasa_epic_url, params=params)
    if response.ok:
        nasa_epic_images = [(datetime.fromisoformat(x['date']), x['image']) for x in response.json()]
        for date, image in nasa_epic_images[:count]:
            image_url = 'https://api.nasa.gov/EPIC/archive/natural/{}/{}/{}/png/{}.png?api_key={}'.format(date.year, date.month, date.day, image, NASA_API_KEY)
            download_images(image_url, 'nasa_{}'.format(image))


if __name__ == '__main__':
    download_images('https://upload.wikimedia.org/wikipedia/commons/3/3f/HST-SM4.jpeg', 'habble')
    fetch_spacex_last_launch()
    fetch_nasa_apod(10)
    fetch_nasa_epic()
