import os
import json

def save_sessdata(sessdata):
    # 将 sessdata 保存到文件中
    with open("sessdata.json", "w") as f:
        json.dump({"sessdata": sessdata}, f)

def load_sessdata():
    # 从文件中加载 sessdata 数据
    if os.path.exists("sessdata.json"):
        with open("sessdata.json", "r") as f:
            data = json.load(f)
            return data.get("sessdata", "")
    else:
        return ""