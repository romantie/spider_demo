import requests
import os
"""url = "http://image.ngchina.com.cn/2018/1214/20181214041129591.jpg"
root = "E://pics//"
path = root + url.split('/')[-1]        #文件名称
try:
    if not os.path.exists(root):            #根目录判断
        os.mkdir(root)      #创建文件
    if not os.path.exists(path):        #文件名
        r = requests.get(url)
        with open(path , 'wb') as f:
            f.write(r.content)
            f.close()
            print("文件保存成功")
    else:
            print("文件已存在")
except:
    print("爬取失败")
"""

url = "https://game.gtimg.cn/images/yxzj/img201606/heroimg/196/196-mobileskin-1.jpg"
root = "E://ajagg//"
path = root + '1234'
try:
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(path):
        r = requests.get(url)
        with open(path, 'wb') as f:
            f.write(r.content)
            f.close()
            print("文件保存成功")
    else:
            print("文件已存在")
except:
    print("爬取失败")