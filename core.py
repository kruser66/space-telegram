import requests
import os


IMAGES_DIR = 'images'


def extarct_the_extension(url):
    return os.path.splitext(url.split('?')[0])[-1]


def download_images(image_url, image_name):
    os.makedirs(IMAGES_DIR, exist_ok=True)

    print('Сохраняем картинку по ссылке {}'.format(image_url.split('?')[0]))
    filename = f'{image_name}{extarct_the_extension(image_url)}'
    response = requests.get(image_url)
    if response.ok:
        with open(os.path.join(IMAGES_DIR, filename), 'wb') as file:
            file.write(response.content)
        print('Картинка сохранена')


if __name__ == '__main__':
    download_images('https://upload.wikimedia.org/wikipedia/commons/3/3f/HST-SM4.jpeg', 'habble')