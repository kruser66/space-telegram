import requests
import os
from datetime import datetime
from dotenv import load_dotenv
from core import download_image, IMAGES_DIR


def fetch_nasa_apod(count=30):
    nasa_apod_url = 'https://api.nasa.gov/planetary/apod'
    params = {
        'api_key': NASA_API_KEY,
        'count': count,
    }
    response = requests.get(nasa_apod_url, params=params)
    if response.ok:
        nasa_apod_images = response.json()
        for data in nasa_apod_images:
            download_image(data['url'], 'nasa_apod_{}'.format(data['date']))


def fetch_nasa_epic(count=5):
    nasa_epic_url = 'https://api.nasa.gov/EPIC/api/natural'
    params = {
        'api_key': NASA_API_KEY,
    }
    response = requests.get(nasa_epic_url, params=params)
    if response.ok:
        nasa_epic_images = [(datetime.fromisoformat(x['date']), x['image']) for x in response.json()]
        for date, image in nasa_epic_images[:count]:
            tepmplate_url = 'https://api.nasa.gov/EPIC/archive/natural/{}/{}/{}/png/{}.png'
            image_url = tepmplate_url.format(date.year, date.month, date.day, image)
            download_image(image_url, 'nasa_{}'.format(image), params)


if __name__ == '__main__':
    load_dotenv()
    NASA_API_KEY = os.getenv('NASA_API_KEY')
    os.makedirs(IMAGES_DIR, exist_ok=True)
    fetch_nasa_apod()
    fetch_nasa_epic()
