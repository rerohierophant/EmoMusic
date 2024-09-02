import base64
import os

from django.shortcuts import render
from langchain_community.chat_models import ChatCoze
from langchain_core.messages import HumanMessage
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import requests
from django.conf import settings

coze_url = "https://api.coze.cn/v1/workflow/run"
coze_headers = {
    "Authorization": "Bearer pat_5qT5weHV5EmXifvWEyAwYCRJhT0MzAihFgNVw1meH0qL0IsTlhFtAURFhSzGJwKM",
    "Content-Type": "application/json",
    "Accept": "*/*",
    "Host": "api.coze.cn",
    "Connection": "keep-alive"
}


def index(request):
    return render(request, 'home_page.html')


@csrf_exempt  # 允许 POST 请求不进行 CSRF 验证
def img2url(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user_query = data.get('query', '')
        img_base64 = data.get('img_base64', '')

        # 解码 Base64 字符串
        image_data = base64.b64decode(img_base64)

        # 定义保存路径（在 template/static 目录下）
        static_dir = os.path.join(settings.BASE_DIR, 'templates/static')
        file_path = os.path.join(static_dir, 'uploaded_image.png')

        # 确保目录存在
        os.makedirs(static_dir, exist_ok=True)

        # 保存为 PNG 文件
        with open(file_path, 'wb') as f:
            f.write(image_data)

        smms_headers = {'Authorization': '8cSPTi6b1l4OfqNb61387CYapubYLB2w'}
        files = {'smfile': open(file_path, 'rb')}
        url = 'https://sm.ms/api/v2/upload'
        res = requests.post(url, files=files, headers=smms_headers).json()
        img_url = res['data']['url']
        payload = {
            "bot_id": "7408538615359389746",
            "workflow_id": "7408530827509858313",
            "parameters": {
                "BOT_USER_INPUT": user_query,
                "img_url": img_url
            }
        }
        response = requests.post(coze_url, headers=coze_headers, json=payload)
        print(response.text)
        data = response.json().get("data")
        result = json.loads(data)["data"]

        return JsonResponse({'response': result})

