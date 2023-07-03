from cid import *

def settings(bvid, page, sessdata):
    params = {
        'bvid': bvid,
        'cid': get_cid(bvid, page),
        'qn': '0',
        'fnval': '80',
        'fnver': '0',
        'fourk': '1'
    }
    headers = {
        'Cookie': f'SESSDATA={sessdata}',
        'referer': 'https://www.bilibili.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}

    return params,headers