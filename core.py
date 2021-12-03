import requests
import os
from urllib.parse import unquote, urlsplit

IMAGES_DIR = 'images'


def extarct_the_extension(url):
    url = unquote(url)
    return os.path.splitext(urlsplit(url).path)[-1]


def download_image(image_url, image_name, params={}):
    filename = f'{image_name}{extarct_the_extension(image_url)}'
    response = requests.get(image_url, params=params)
    if response.ok:
        with open(os.path.join(IMAGES_DIR, filename), 'wb') as file:
            file.write(response.content)


def main():
    url = 'https://upload.wikimedia.org/wikipedia/commons/3/3f/HST-SM4.jpeg'
    os.makedirs(IMAGES_DIR, exist_ok=True)
    download_image(url, 'habble')


if __name__ == '__main__':
    main()
