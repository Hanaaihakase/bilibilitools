import requests
import json

def get_data_without_headers(url, params):
    response = requests.get(url, params=params)

    data = response.content
    data = json.loads(data)

    print(data)
    return data    

def get_data(url, params, headers):
    response = requests.get(url, params=params, headers=headers)

    data = response.content
    data = json.loads(data)

    print(data)
    return data 
