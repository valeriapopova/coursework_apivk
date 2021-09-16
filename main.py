import requests
import time
from tqdm import tqdm
import json
from ya import YD
from pprint import pprint

version = '5.131'
URL = 'https://api.vk.com/method/photos.get'
token = '958eb5d439726565e9333aa30e50e0f937ee432e927f0dbd541c541887d919a7c56f95c04217915c32008'
id = '552934290'

def getting_photos():
    params = {
        'owner_id': id,
        'album_id': 'profile',
        'extended': '1',
        'access_token': token,
         'v': version,
        'feed': ''
    }
    res = requests.get(URL, params=params, timeout=5)
    return res.json()



pprint(getting_photos())


def photos_list():
    photos_json = getting_photos()['response']['items']
    photos_dict = {}
    for i in photos_json:
        likes = f"{i['likes']['count']}.jpg"
        size = i['sizes'][-1]
        if likes in photos_dict:
            photos_dict[f"{i['date']}.jpg"] = size
        else:
            photos_dict[likes] = size

    return photos_dict


pprint(photos_list())



if __name__ == '__main__':
    vk = photos_list().keys()
    vk_path = photos_list().values()
    ya_token = ''
    uploader = YD(ya_token)
    result = uploader.upload_file_to_disk(vk_path, vk)
    pprint(result)