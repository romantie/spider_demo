import requests
import json
import re
import os

#导入josn文件

url = "https://pvp.qq.com/web201605/js/herolist.json"
head = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.5514.400 QQBrowser/10.1.1614.400'
}
html = requests.get(url,headers = head)
html_json = html.json()

hero_name = list(map(lambda x:x["cname"],html_json) ) #英雄的名字
hero_num = list(map(lambda x:x["ename"],html_json) ) #英雄对应的数字编号

def main():
    li=0
    for v in hero_num:
        os.mkdir("E://wzry//"+hero_name[li])    #创建目录
        os.chdir("E://wzry//"+hero_name[li])    #改变当前工作目录
        li = li+1
        for u in range(12):
            onehero_url = "https://game.gtimg.cn/images/yxzj/img201606/heroimg/"+str(v)+"/"+str(v)+"-mobileskin-"+str(u)+".jpg"
            try:
                r = requests.get(onehero_url,timeout = 10)
                if r.status_code == 200:
                    iv = re.split('-',onehero_url)
                    open(iv[-1],'wb').write(r.content)
                    print("保存成功")
            except:
                return ''

main()

