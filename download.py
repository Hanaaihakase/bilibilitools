import requests
import os
import subprocess
import time
from setting import *
from data import *
from title import *

def download_from_url(url, path, title, type, type2, headers, info):
    # 下载函数
    max_retry = 5
    retry_interval = 3
    chunk_size = 1024

    for i in range(max_retry):
        try:
            response = requests.get(url, headers=headers, stream=True, timeout=30)
            response.raise_for_status()
            length = int(response.headers.get('content-length', 0))

            os.makedirs(path, exist_ok=True)
            with open(os.path.join(path, f'{title}_{type}.{type2}'), 'wb') as f:
                process = 0
                for chunk in response.iter_content(chunk_size=chunk_size):
                    if chunk:
                        process += len(chunk)
                        print(f'Download {info} {process} / {length}')
                        f.write(chunk)
            break
        except requests.exceptions.RequestException as e:
            print(f'Download failed, retrying in {retry_interval} seconds...')
            time.sleep(retry_interval)
            continue

def download_from_data(bvid, data, save_path, save_title, save_type1, save_type2, headers):
    # Get the video url and download the video of mp4
    url = data["data"]["dash"][save_type1][0]["baseUrl"]
    print(f"The {save_type1} url of {bvid} is {url}")
    download_from_url(url, save_path, save_title, save_type1, save_type2, headers, save_type1)

def download_video(bvid, page, sessdata):
    url = 'https://api.bilibili.com/x/player/playurl'
    params,headers = settings(bvid, page, sessdata)

    # Get the data
    data = get_data(url, params, headers)

    bv_title = bvid
    save_path = fr".\BV"
    title = get_title(bvid)
    page_title = get_page_title(bvid, page, sessdata)
    save_title = f"{title}_{page_title}_{bv_title}_{page}"

    # Get the video url and download the video of mp4
    download_from_data(bvid, data, save_path, save_title, "video", "m4s", headers)

    # Get the audio url and download the audio of mp4
    download_from_data(bvid, data, save_path, save_title, "audio", "m4s", headers) 

    # Combine the video and audio to mp4
    subprocess.call(['ffmpeg', '-i', os.path.join(save_path, f'{save_title}_video.m4s'), '-i', os.path.join(save_path, f'{save_title}_audio.m4s'), '-c:v', 'copy', '-c:a', 'copy', '-f', 'mp4', os.path.join(save_path, f'{save_title}.mp4')])
    print(f"The dowloading of {save_title}.mp4 has been done!")

def download_audio(bvid, page, sessdata):
    url = 'https://api.bilibili.com/x/player/playurl'
    params,headers = settings(bvid, page, sessdata)

    # Get the data
    data = get_data(url, params, headers)

    bv_title = bvid
    save_path = fr".\BV"
    title = get_title(bvid)
    page_title = get_page_title(bvid, page, sessdata)
    save_title = f"{title}_{page_title}_{bv_title}_{page}"

    # Get the audio url and download the audio of mp4
    download_from_data(bvid, data, save_path, save_title, "audio", "m4a", headers) 
