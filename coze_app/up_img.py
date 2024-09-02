# 8cSPTi6b1l4OfqNb61387CYapubYLB2w

import requests
import json


def upload(path):
    headers = {'Authorization': '8cSPTi6b1l4OfqNb61387CYapubYLB2w'}
    files = {'smfile': open(path, 'rb')}
    url = 'https://sm.ms/api/v2/upload'
    res = requests.post(url, files=files, headers=headers).json()

    print(res['data']['url'])


if __name__ == "__main__":
    upload('23.png')
