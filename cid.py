import requests

def get_cid(bvid,page):
    url = 'https://api.bilibili.com/x/player/pagelist'
    params = {'bvid': f'{bvid}'}

    response = requests.get(url, params=params)
    json_data = response.json()

    print(json_data)
    cid = json_data["data"][page]["cid"]

    print(f"The cid of {bvid} of page number {page} is {cid}")
    return cid

def get_cid_dict(bvid):
    # Input the bvid to get a dictionary of cids and their page numbers

    url = 'https://api.bilibili.com/x/player/pagelist'
    params = {'bvid': f'{bvid}'}

    response = requests.get(url, params=params)
    json_data = response.json()

    cid_dict = {}
    for page in json_data["data"]:
        cid_dict[page["page"]] = page["cid"]
    
    return cid_dict

def get_max_page(bvid):
    # Input the bvid to get the maximum page number 

    url = 'https://api.bilibili.com/x/player/pagelist'
    params = {'bvid': f'{bvid}'}

    response = requests.get(url, params=params)
    json_data = response.json()

    pages = [page["page"] for page in json_data["data"]]
    max_page = max(pages)
    
    print(f"The maximum page number of {bvid} is {max_page}")
    return int(max_page)