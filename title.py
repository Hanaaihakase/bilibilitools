import re
import requests
import json
from setting import *
from data import *

def retitle(title):
    # 匹配非法字符，并将其替换为空格
    title = re.sub(r'[\\/:*?"<>|]', ' ', title)
    # 将连续的空格替换为单个空格
    title = re.sub(r'\s+', ' ', title)
    # 将开头和结尾处的空格去掉
    title = title.strip()
    return title

def get_title(bvid):
    url = 'https://api.bilibili.com/x/web-interface/view'
    params = {'bvid': f'{bvid}'}

    data = get_data_without_headers(url, params)

    title = data["data"]["title"]
    title = retitle(title)
    print(f"The title is {title}")
    return title

def get_page_title(bvid, page, sessdata):
    url = 'https://api.bilibili.com/x/web-interface/view'
    params,headers = settings(bvid, page, sessdata)

    data = get_data(url,params,headers)

    title = data["data"]["pages"][page]["part"]
    # Replace the illegal string
    title = retitle(title)

    print(f"The page title is {title}")
    return title
