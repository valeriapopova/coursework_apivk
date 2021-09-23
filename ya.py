import requests


class YD:

    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def create_folder(self, folder):
        url = "https://cloud-api.yandex.net/v1/disk/resources"
        headers = self.get_headers()
        params = {
            'path': folder
        }
        response = requests.put(url, headers=headers, params=params)
        return response

    def upload_(self, file_path, file_name):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        params = {"path": f'vk_photos/{file_name}', "url": file_path, "overwrite": "true"}
        response = requests.post(upload_url, headers=headers, params=params)
        res = response.json()
        return res
