from django.shortcuts import render
from langchain_community.chat_models import ChatCoze
from langchain_core.messages import HumanMessage
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json


def index(request):
    return render(request, 'home_page.html')


def get_coze_response(query):
    chat = ChatCoze(
        coze_api_base="https://api.coze.cn",
        coze_api_key="pat_C7bpuX5taxZ37hRoMjZ1UiU3iyObJ1nsBjOLUr1jTM05zYbEHb5a1juD3zgTYmE7",
        bot_id="7408432565092155429",
        user="酸菜且多余",
        conversation_id="123",
        streaming=True,
    )
    print(chat([HumanMessage(content=query)]).content)
    return chat([HumanMessage(content=query)]).content


@csrf_exempt  # 允许 POST 请求不进行 CSRF 验证
def coze_response_view(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user_query = data.get('query', '')

        # 调用 get_coze_response 获取模型的回应
        response = get_coze_response(user_query)

        return JsonResponse({'response': response})

    return JsonResponse({'error': 'Invalid request method'}, status=400)