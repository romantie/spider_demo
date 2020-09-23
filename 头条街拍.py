import requests
from urllib.parse import urlencode
from bs4 import BeautifulSoup
import json

def get_page(offset):
    params = {
            'aid' : '24',
            'app_name' : 'web_search',
            'offset' : 'offset',
            'format' : 'json',
            'keyword' : '%E8%A1%97%E6%8B%8D%E7%BE%8E%E5%9B%BE',
            'autoload': 'ture',
            'count' : '20',
            'cur_tab' : '1',
            'from' : 'search_ta',
            'pd': 'synthesis',
            'timestamp':'1553308377357'
        }
    url = 'http://www.toutiao.com/api/search/content/?' + urlencode(params)
    #https://www.toutiao.com/api/search/content/?aid=24&app_name=web_search&offset=0&format=json&keyword=%E8%A1%97%E6%8B%8D%E7%BE%8E%E5%9B%BE&autoload=true&count=20&en_qc=1&cur_tab=1&from=search_tab&pd=synthesis&timestamp=1553308377357

    headers = {
        'user-agent' :'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
        'referer':'https://www.toutiao.com/search/?keyword=%E8%A1%97%E6%8B%8D%E7%BE%8E%E5%9B%BE',
        'x-requested-with':'XMLHttpRequest'
    }

    try:
        response = requests.get(url,headers= headers)
        if response.status_code == 200:
            return response.json()
    except requests.ConnectionError:
        return None

def get_images(json):
    if json.get('data'):
        for itme in json.get('data'):
            titles = itme.get('title')
            for title in titles:
                return title



def main():
    json = get_page(0)
    image = get_images(json)
    print(image)

main()