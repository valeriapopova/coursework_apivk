import requests
from pprint import pprint

version = '5.131'
URL = 'https://api.vk.com/method/photos.get'
token = '958eb5d439726565e9333aa30e50e0f937ee432e927f0dbd541c541887d919a7c56f95c04217915c32008'


def getting_photos():
    params = {
        'owner_id': '552934290',
        'album_id': 'profile',
        'extended': '1',
        'access_token': token,
         'v': version,
        'feed': ''
    }
    res = requests.get(URL, params=params)
    return res.json()


pprint(getting_photos())


def photos_list():
    photos = []
    for values in getting_photos().values():
        for likes in values['items']:
            # photos.append({
            #     'file_name': likes['likes']['count'],
            #     # 'size': likes['sizes']['type']['-1']
            # })
            if likes['likes']['count'] not in photos:
                photos.append({
                    'file_name': likes['likes']['count']
                })
            else:
                photos.append({
                    'file_name': likes['date']
                })
    return photos


print(photos_list())


