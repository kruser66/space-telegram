import os
import requests
from core import download_image, IMAGES_DIR


def fetch_spacex_last_launch():
    api_url = 'https://api.spacexdata.com/v3/launches/latest'
    response = requests.get(api_url)

    if response.ok:
        json_data = response.json()['links']['flickr_images']
        for image_number, image in enumerate(json_data, start=1):
            download_image(image, 'spacex_last_{}'.format(str(image_number)))


def fetch_spacex_launch(launch):
    api_url = 'https://api.spacexdata.com/v3/launches/{}'
    response = requests.get(api_url.format(str(launch)))

    if response.ok:
        json_data = response.json()['links']['flickr_images']
        for image_number, image in enumerate(json_data, start=1):
            filename = 'spacex_{}_{}'.format(str(launch), str(image_number))
            download_image(image, filename)


if __name__ == '__main__':
    os.makedirs(IMAGES_DIR, exist_ok=True)
    fetch_spacex_last_launch()
    fetch_spacex_launch(33)
