import re
import requests
import json

def retitle(title):
    # 匹配非法字符，并将其替换为空格
    title = re.sub(r'[\\/:*?"<>|]', ' ', title)
    # 将连续的空格替换为单个空格
    title = re.sub(r'\s+', ' ', title)
    # 将开头和结尾处的空格去掉
    title = title.strip()
    return title

def get_title(bvid,page):
    url = 'https://api.bilibili.com/x/web-interface/view'
    params = {'bvid': f'{bvid}'}
    headers = {'referer': 'https://www.bilibili.com'}

    response = requests.get(url, params=params,headers=headers)

    info = response.content
    info = json.loads(info)

    title = info["data"]["pages"][page]["part"]
    # Replace the illegal string
    title = retitle(title)

    print(f"The title is {title}")
    return title
