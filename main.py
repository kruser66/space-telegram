import requests
import os
# from dotenv import load_dotenv
# from instabot import Bot
# import random
# import glob

IMAGES_DIR = 'images'
if not os.path.exists(IMAGES_DIR):
    os.makedirs(IMAGES_DIR)



def download_images(image_url, image_name):
    print('Сохраняем картинку по ссылке {}'.format(image_url))
    filename = image_name + os.path.splitext(image_url.split('?')[0])[1]
    response = requests.get(image_url)
    if response.ok:
        with open(os.path.join(IMAGES_DIR, filename), 'wb') as file:
            file.write(response.content)
        print('Картинка сохранена')


def fetch_spacex_last_launch():
    response = requests.get('https://api.spacexdata.com/v3/launches/latest')
    images = response.json()['links']['flickr_images']
    for image_number, image in enumerate(images):
        download_images(image, 'spacex' + str(image_number + 1))


def fetch_hubble_image(image_id):
    hubble_url = 'http://hubblesite.org/api/v3/image/' + str(image_id)
    response = requests.get(hubble_url)
    if response.ok:
        hubble_images = response.json()['image_files']
        images = [image['file_url'] for image in hubble_images]
        download_images(images[-1], 'hubble_' + str(image_id))


if __name__ == '__main__':
    download_images('https://upload.wikimedia.org/wikipedia/commons/3/3f/HST-SM4.jpeg', 'habble')
