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
        "img_url": 'https://s2.loli.net/2024/08/30/dBO9cXo5PLHKSF1.png'
    }
}
print(payload)
response = requests.post(url, headers=headers, json=payload)
print("coze："+response.text)
data = response.json().get("data")
print(json.loads(data)["data"])

