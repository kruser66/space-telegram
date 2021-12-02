import requests
from core import download_image, make_images_dir, IMAGES_DIR


def fetch_spacex_last_launch():
    api_url = 'https://api.spacexdata.com/v3/launches/latest'
    response = requests.get(api_url)

    if response.ok:
        json_data = response.json()['links']['flickr_images']
        for image_number, image in enumerate(json_data, start=1):
            download_image(image, 'spacex_last_{}'.format(str(image_number)))
    else:
        print('Нет данных о последнем запуске')


def fetch_spacex_launch(launch):
    api_url = 'https://api.spacexdata.com/v3/launches/{}'
    response = requests.get(api_url.format(str(launch)))

    if response.ok:
        print('Загружаем изображения запуска номер: {}'.format(str(launch)))
        json_data = response.json()['links']['flickr_images']
        for image_number, image in enumerate(json_data, start=1):
            filename = 'spacex_{}_{}'.format(str(launch), str(image_number))
            download_image(image, filename)
    else:
        print('Нет данных о запуске номер: {}'.format(str(launch)))


if __name__ == '__main__':
    make_images_dir(IMAGES_DIR)
    fetch_spacex_last_launch()
    fetch_spacex_launch(33)
