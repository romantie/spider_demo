import requests
import time


def getHtml(url):

    try:

        r=requests.get(url,timeout=10)

        r.raise_for_status

        return 'ok'

    except:

        return'失败'



url='https://202.197.224.171/zfca/login?service=http%3A%2F%2F202.197.224.171%2Fportal.do'

t1=time.time()

try:

    for i in range(3):

        getHtml(url)

    t2=time.time()

    print(t2-t1)

    print("爬取成功")

except:

    print("爬取失败")

