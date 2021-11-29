import requests
from core import download_images


IMAGES_DIR = 'images'


def fetch_spacex_last_launch():
    # ищем последний запуск
    response = requests.get('https://api.spacexdata.com/v3/launches/latest')

    # загружаем картинки запуска 
    if response.ok:
        for image_number, image in enumerate(response.json()['links']['flickr_images']):
            download_images(image, 'spacex_last_{}'.format(str(image_number + 1)))
    else:
        print('Нет данных о последнем запуске')


def fetch_spacex_launch(launch):
    response = requests.get('https://api.spacexdata.com/v3/launches/{}'.format(str(launch)))

    # загружаем картинки запуска
    if response.ok:
        for image_number, image in enumerate(response.json()['links']['flickr_images']):
            download_images(image, 'spacex_'.join(str(image_number + 1)))
    else:
        print('Нет данных о запуске номер {}'.format(str(launch)))


if __name__ == '__main__':
    # example collect images
    fetch_spacex_last_launch()
    fetch_spacex_launch(33)
