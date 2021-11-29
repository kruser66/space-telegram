import requests
import os
from datetime import datetime
from dotenv import load_dotenv
from core import download_images


IMAGES_DIR = 'images'

# nasa API key from https://api.nasa.gov/
# NASA_API_KEY = 'Your API_key'
load_dotenv()
NASA_API_KEY = os.getenv('NASA_API_KEY')


# One of the most popular websites at NASA is the Astronomy Picture of the Day
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
            download_images(data['url'], 'nasa_apod_{}'.format(data['date']))


# The EPIC API provides information on the daily imagery collected by DSCOVR's Earth Polychromatic Imaging Camera (EPIC)
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
    # example to collect images
    fetch_nasa_apod()
    # fetch_nasa_epic()
