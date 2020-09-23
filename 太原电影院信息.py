import requests
from bs4 import BeautifulSoup

def get_onepage(url):
    try:
        headers = {

            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.5514.400 QQBrowser/10.1.1614.400'
        }

        response = requests.get(url,headers = headers)
        if response.status_code == 200:
            return response.text
        else:
            response.reason
    except:
        return ""

def main():

     url = "https://maoyan.com/cinemas"
     html = get_onepage(url)
     print(html)

main()

