import requests
import json

url = "https://api.coze.cn/v1/workflow/run"
headers = {
    "Authorization": "Bearer pat_5qT5weHV5EmXifvWEyAwYCRJhT0MzAihFgNVw1meH0qL0IsTlhFtAURFhSzGJwKM",
    "Content-Type": "application/json",
    "Accept": "*/*",
    "Host": "api.coze.cn",
    "Connection": "keep-alive"
}

payload = {
    "bot_id": "7408538615359389746",
    "workflow_id": "7408530827509858313",
    "parameters": {
        "BOT_USER_INPUT": "",
        "img_url": "https://p9-bot-sign.byteimg.com/tos-cn-i-v4nquku3lp/e409130e18134edd81ac122a2778075e.jpg~tplv-v4nquku3lp-image.image?rk3s=68e6b6b5&x-expires=1727370417&x-signature=ZEU1ESTaUmgmrLpM0rYcAkbxFfE%3D"
    }
}

response = requests.post(url, headers=headers, json=payload)
data = response.json().get("data")
print(json.loads(data)["data"])