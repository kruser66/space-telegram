import requests
import os
from datetime import datetime
from dotenv import load_dotenv
from core import download_image, IMAGES_DIR


def fetch_nasa_apod(api_key, count=30):
    nasa_apod_url = 'https://api.nasa.gov/planetary/apod'
    params = {
        'api_key': api_key,
        'count': count,
    }
    response = requests.get(nasa_apod_url, params=params)
    if response.ok:
        nasa_apod_images = response.json()
        for data in nasa_apod_images:
            download_image(data['url'], 'nasa_apod_{}'.format(data['date']))


def fetch_nasa_epic(api_key, count=5):
    nasa_epic_url = 'https://api.nasa.gov/EPIC/api/natural'
    params = {
        'api_key': api_key,
    }
    response = requests.get(nasa_epic_url, params=params)
    if response.ok:
        epic_images = [(url['date'], url['image']) for url in response.json()]
        for date_url, image in epic_images[:count]:
            date = datetime.fromisoformat(date_url)
            str_url = 'https://api.nasa.gov/EPIC/archive/natural/{}/{}/{}/png/{}.png'
            image_url = str_url.format(date.year, date.month, date.day, image)
            download_image(image_url, 'nasa_{}'.format(image), params)


if __name__ == '__main__':
    load_dotenv()
    nasa_api_key = os.getenv('NASA_API_KEY')
    os.makedirs(IMAGES_DIR, exist_ok=True)
    fetch_nasa_apod(nasa_api_key)
    fetch_nasa_epic(nasa_api_key)
