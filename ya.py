import requests
from pprint import pprint


class YD:

    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def get_upload_link(self, file_path):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        params = {"path": file_path, "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params)
        pprint(response.json())
        return response.json()

    def upload_file_to_disk(self, file_path, filename):
        href = self.get_upload_link(file_path=file_path).get("href", "")
        response = requests.put(href, filename)
        response.raise_for_status()
        if response.status_code == 201:
            print("Success")


