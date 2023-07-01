import requests

def get_cid(bvid):
    # Input the bvid to get the cid 

    url = 'https://api.bilibili.com/x/player/pagelist'
    params = {'bvid': f'{bvid}'}

    response = requests.get(url, params=params)
    json_data = response.json()
    cid = json_data["data"][0]["cid"]

    print(f"The cid of {bvid} is {cid}")
    return cid
