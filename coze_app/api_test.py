import os
from coze import Coze
os.environ['COZE_API_TOKEN'] = 'pat_C7bpuX5taxZ37hRoMjZ1UiU3iyObJ1nsBjOLUr1jTM05zYbEHb5a1juD3zgTYmE7'
os.environ['COZE_BOT_ID'] = "7407817922460188707"

# text: 7408432565092155429

chat = Coze(
    api_token=os.environ['COZE_API_TOKEN'],
    bot_id=os.environ['COZE_BOT_ID'],
    max_chat_rounds=20,
    stream=True
)

response = chat('北京最新的高级产品经理岗位有推荐吗')

print(response)
