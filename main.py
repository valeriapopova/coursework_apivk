import requests
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
    photos = []
    for values in getting_photos().values():
        for likes in values['items']:
            if likes['likes']['count'] not in photos:
                photos.append({
                    'file_name': f"{likes['likes']['count']}.jpg",
                    'size': likes['sizes'][-1]['type'],
                    'size url': likes['sizes'][-1]['url']
                 })
            else:
                photos.append({
                    'file_name': f"{likes['date']}.jpg",
                    'size': likes['sizes'][-1]['type'],
                    'size url': likes['sizes'][-1]['url']
                    })
    return photos


pprint(photos_list())

if __name__ == '__main__':

    vk = photos_list['file_name']
    vk_path = photos_list['size url']
    ya_token = ''
    uploader = YD(ya_token)
    result = uploader.upload_file_to_disk(vk_path, vk)
    pprint(result)