import requests
import json

def get_data(url,params,headers):
    response = requests.get(url, params=params,headers=headers)

    data = response.content
    data = json.loads(data)

    print(data)
    return data 
