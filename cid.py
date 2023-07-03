from data import *

def get_cid(bvid, page):
    url = 'https://api.bilibili.com/x/player/pagelist'
    params = {'bvid': f'{bvid}'}

    data = get_data_without_headers(url, params)
    cid = data["data"][page]["cid"]

    print(f"The cid of {bvid} of page number {page} is {cid}")
    return cid

def get_max_page(bvid):
    # Input the bvid to get the maximum page number 

    url = 'https://api.bilibili.com/x/player/pagelist'
    params = {'bvid': f'{bvid}'}

    data = get_data_without_headers(url, params)
    pages = [page["page"] for page in data["data"]]
    max_page = max(pages)

    print(f"The maximum page number of {bvid} is {max_page}")
    return max_page