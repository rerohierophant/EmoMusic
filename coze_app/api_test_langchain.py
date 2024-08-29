from langchain_community.chat_models import ChatCoze
from langchain_core.messages import HumanMessage

chat = ChatCoze(
    coze_api_base="https://api.coze.cn",
    coze_api_key="pat_C7bpuX5taxZ37hRoMjZ1UiU3iyObJ1nsBjOLUr1jTM05zYbEHb5a1juD3zgTYmE7",
    bot_id="7408432565092155429",
    user="酸菜且多余",
    conversation_id="123",
    streaming=True,
)

print(chat([HumanMessage(content="什么是扣子(coze)")]).content)
