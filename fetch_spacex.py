import requests
from core import download_image


IMAGES_DIR = 'images'


def fetch_spacex_last_launch():
    response = requests.get('https://api.spacexdata.com/v3/launches/latest')

    if response.ok:
        for image_number, image in enumerate(response.json()['links']['flickr_images'], start=1):
            download_image(image, 'spacex_last_{}'.format(str(image_number)))
    else:
        print('Нет данных о последнем запуске')


def fetch_spacex_launch(launch):
    response = requests.get('https://api.spacexdata.com/v3/launches/{}'.format(str(launch)))

    if response.ok:
        print('Загружаем изображения запуска номер: {}'.format(str(launch)))
        for image_number, image in enumerate(response.json()['links']['flickr_images'], start=1):
            download_image(image, 'spacex_launch{}_{}'.format(str(launch), str(image_number)))
    else:
        print('Нет данных о запуске номер: {}'.format(str(launch)))


if __name__ == '__main__':
    fetch_spacex_last_launch()
    fetch_spacex_launch(33)
