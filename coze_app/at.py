import requests
import json
import re

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

# response = requests.post(url, headers=headers, json=payload)
# data = response.json().get("data")
# print(json.loads(data)["data"])
#
# result = json.loads(data)["data"]
result = '''-房子外观描述：房子外观方正，屋顶线条简洁，烟囱细长，整体给人一种简洁而稳定的感觉。
对于这幅画中的树，描述如下：很小的树、轻描淡写的树、单线条的树、简单的单线条树枝、树枝在树干底部生长、树叶稀少。
-树外观描述：这棵树是风景画中的树，大树冠，树冠呈云状或球形，树叶浓密，树干粗大，用曲线形线条描画树干表面。
-人外观描述：画中的人外观较为简单，没有过多的细节描绘，可能是一个比较单纯的人。人处于画面的右侧，说明其可能比较关注未来和外部世界。人的身体比例较为协调，没有明显的夸张之处，显示出一种平衡感。人的动作自然，没有特别的紧张或僵硬感，表明其心态较为放松。人的表情不清晰，可能代表其内心世界较为神秘，不太容易被他人了解。人的服装也没有具体描绘，暗示其对自我形象的认知比较模糊。
-心理状态：有干劲但情绪波动大，对外界有警戒心，既想适应社会又在人际交往中有不安。
-相关建议：尝试更加真诚地与他人交流，分享自己的真实想法，同时学会稳定情绪，减少幻想。
-音乐prompt：舒缓的钢琴旋律，夹杂着轻柔的海浪声和鸟鸣声
-用户心情：思'''

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

# 输出结果
print("房子外观描述:", house_desc)
print("树外观描述:", tree_desc)
print("人外观描述:", person_desc)
print("心理状态:", mental_state)
print("相关建议:", suggestion)
print("音乐prompt:", music_prompt)
print("用户心情:", user_mood)
