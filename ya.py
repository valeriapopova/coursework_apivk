import requests
path = 'vk_photos/'



class YD:

    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def upload_(self, file_path, file_name):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        params = {"path": f'{path}{file_name}', "url": file_path, "overwrite": "true"}
        response = requests.post(upload_url, headers=headers, params=params)
        res = response.json()
        return res