import base64
import os
import re

from django.shortcuts import redirect
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

session = {}
user_mood = ''

def index(request):
    return render(request, 'index.html')


def paint(request):
    return render(request, 'paint.html')


def loading(request):
    return render(request, 'loading.html')


@csrf_exempt  # 允许 POST 请求不进行 CSRF 验证
def htp(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        # user_query = data.get('query', '')
        img_base64 = data.get('img_base64', '')

        # 解码 Base64 字符串
        image_data = base64.b64decode(img_base64)

        # 定义保存路径（在 template/static 目录下）
        static_dir = os.path.join(settings.BASE_DIR, 'templates/static/sketch')
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
        print("\n")
        print(res)
        print("\n")
        img_url = res['data']['url']
        payload = {
            "bot_id": "7408538615359389746",
            "workflow_id": "7408530827509858313",
            "parameters": {
                "BOT_USER_INPUT": "",
                "img_url": img_url
            }
        }
        response = requests.post(coze_url, headers=coze_headers, json=payload)
        print(response.text)
        data = response.json().get("data")
        result = json.loads(data)["data"]

        # 将结果存储到 session 中
        session['result'] = result
        session['status'] = 'done'  # 标记处理状态为完成

        return JsonResponse({'status': 'processing'})


def htp_view(request):
    # 从 session 获取结果
    result = session.get('result', '没有结果')  # 如果 result 不存在，返回默认值
    session['status'] = ''
    # 将 result 传递给模板

    # 定义正则表达式来匹配每个部分的描述
    pattern = {
        'house_desc': r"-房子外观描述：(.*?)\n",
        'tree_desc': r"-树外观描述：(.*?)\n",
        'person_desc': r"-人外观描述：(.*?)\n",
        'mental_state': r"-心理状态：(.*?)\n",
        'suggestion': r"-相关建议：(.*?)\n",
        'music_prompt': r"-音乐prompt：(.*?)\n",
        'user_mood': r"-用户心情：(.*)"
    }

    # 使用正则表达式提取信息
    info = {}
    for key, regex in pattern.items():
        match = re.search(regex, result, re.DOTALL)
        if match:
            info[key] = match.group(1).strip()

    # 提取结果
    house_desc = info.get('house_desc')
    tree_desc = info.get('tree_desc')
    person_desc = info.get('person_desc')
    mental_state = info.get('mental_state')
    suggestion = info.get('suggestion')
    music_prompt = info.get('music_prompt')
    user_mood = info.get('user_mood')

    return render(request, 'htp.html', {
        'result': result,
        'house_desc': house_desc,
        'tree_desc': tree_desc,
        'person_desc': person_desc,
        'mental_state': mental_state,
        'suggestion': suggestion,
        'music_prompt': music_prompt,
        'user_mood': user_mood
    })


def flower(request):
    return render(request, 'flower.html', {'user_mood': user_mood})


def bigscreen(request):
    return render(request, 'bigscreen.html')


def check_status(request):
    status = session.get('status', 'processing')  # 获取处理状态
    return JsonResponse({'status': status})




