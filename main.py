import requests
from datetime import datetime
from ya import YD
from pprint import pprint
from tqdm import tqdm
import time

version = '5.131'
URL = 'https://api.vk.com/method/photos.get'
token = ''
id_or_username = ''


def getting_photos():
    params = {
        'owner_ids': id_or_username,
        'album_id': 'profile',
        'extended': '1',
        'access_token': token,
         'v': version,
        'feed': ''
    }
    res = requests.get(URL, params=params, timeout=5)
    return res.json()


def photos_list():
    photos_json = getting_photos()['response']['items']
    photos_dict = {}
    for photo in photos_json:
        likes = f"{photo['likes']['count']}.jpg"
        size = photo['sizes'][-1]['url']
        if likes in photos_dict:
            d = datetime.fromtimestamp(photo['date']).strftime('%m-%d-%y %H-%M-%S')
            photos_dict[f"{d}.jpg"] = size
        else:
            photos_dict[likes] = size

    return photos_dict


# pprint(photos_list())


if __name__ == '__main__':
    ya_token = ''
    uploader = YD(ya_token)
    uploader.create_folder('vk_photos')
    for item, file in photos_list().items():
        result = uploader.upload_(file, item)
        for i in tqdm(result, desc='Photo', unit=' photo'):
            time.sleep(0.25)
        pprint(result)
