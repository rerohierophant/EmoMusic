from django.shortcuts import render
from langchain_community.chat_models import ChatCoze
from langchain_core.messages import HumanMessage
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import requests

url = "https://api.coze.cn/v1/workflow/run"
headers = {
    "Authorization": "Bearer pat_5qT5weHV5EmXifvWEyAwYCRJhT0MzAihFgNVw1meH0qL0IsTlhFtAURFhSzGJwKM",
    "Content-Type": "application/json",
    "Accept": "*/*",
    "Host": "api.coze.cn",
    "Connection": "keep-alive"
}


def index(request):
    return render(request, 'home_page.html')


def get_coze_response(query, img_url):
    payload = {
        "bot_id": "7408538615359389746",
        "workflow_id": "7408530827509858313",
        "parameters": {
            "BOT_USER_INPUT": query,
            "img_url": img_url
        }
    }

    response = requests.post(url, headers=headers, json=payload)
    data = response.json().get("data")
    print(response.text)
    return json.loads(data)["data"]


@csrf_exempt  # 允许 POST 请求不进行 CSRF 验证
def coze_response_view(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user_query = data.get('query', '')
        user_img = data.get('img_url')
        # 调用 get_coze_response 获取模型的回应
        response = get_coze_response(user_query, user_img)

        return JsonResponse({'response': response})

    return JsonResponse({'error': 'Invalid request method'}, status=400)
