import requests
from bs4 import BeautifulSoup
import csv

def get_onepage(url):   #获取单个页面
    try:
        headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.5514.400 QQBrowser/10.1.1614.400'
                    }
        response = requests.get(url,headers = headers)
        response.encoding = response.apparent_encoding
        if response.status_code ==200:
            return response.text
        else:
            response.reason
    except:
        return ""

def parse_onepage(html):    #解析网页
    soup = BeautifulSoup(html,"html.parser")
    itmes = range(10)
    for itme in itmes:  #构造生成器
        yield{

            'rank' : soup.find_all(class_ = 'board-index')[itme].string,
            #'picqs' : soup.find_all(name='img',attrs={'class':'board-img'})[itme].string,
            'name' : soup.find_all(name='p',attrs={'class':'name'})[itme].string.strip("'"),
            'star' : soup.find_all(name='p',attrs={'class':'star'})[itme].string.strip()[3:],
            'time' : soup.find_all(class_ = 'releasetime')[itme].string[5:].split('(',1)[0],
            'area' : soup.find_all(class_ = 'releasetime')[itme].string[15:].lstrip('(').rstrip(')'),
            'score': (soup.find_all(name='i',attrs={'class':'integer'})[itme].string +
                      soup.find_all(name='i',attrs={'class':'fraction'})[itme].string               #获取电影信息
                      )

        }

def write_to_file(itme):    #写入csv文件中
    with open('猫眼top100.csv','a',encoding='ansi',newline='') as f :
            fieldnames = ['rank','picqs','name','star','time','area','score']   #表头
            w = csv.DictWriter(f,fieldnames=fieldnames)
            w.writerow(itme)

def main(offset):
    url = "https://maoyan.com/board/4?offset=" + str(offset)
    html = get_onepage(url)
    for itme in parse_onepage(html):
        write_to_file(itme)



if __name__ == '__main__':
    for i in range(10):
        main(offset=i*10)





