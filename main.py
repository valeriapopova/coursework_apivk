import requests
from datetime import datetime
from ya import YD
from pprint import pprint
from tqdm import tqdm
import time
import json

version = '5.131'
URL = 'https://api.vk.com/method/photos.get'
id_ = input('Введите username или id:')
count_ = input('Введите кол-во фото при загрузке:')
token = ''


def get_id():
    _get_id = {}
    url_ = 'https://api.vk.com/method/users.get'
    params = {
        'user_ids': id_,
        'access_token': token,
        'v': version
    }
    response = requests.get(url_, params=params).json()
    for items in response['response']:
        user_id = items['id']
        _get_id = {'id': user_id}
    return _get_id


def getting_photos():
    data = get_id()
    for value in data.items():
        params = {
            'owner_id': value,
            'album_id': 'profile',
            'extended': '1',
            'access_token': token,
            'v': version,
            'feed': '',
            'count': count_
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
    p = json.dumps(photos_list(), indent=4, ensure_ascii=False)
    print(p)
