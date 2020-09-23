import requests
from bs4 import BeautifulSoup

url = "http://www.weather.com.cn/textFC/hb.shtml"
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36"
}
response = requests.get(url=url,headers=headers)
text = response.content
#print(text)
soup = BeautifulSoup(text,"html.parser")
#print(soup.prettify())

table_1s = soup.find_all("table")
#print(table_1s)
list1 = []
for table_1 in table_1s:
    trs = table_1.find_all("tr")[2:]
    for index,tr in enumerate(trs):
        tds = tr.find_all("td")
        if index==0:
            province = list(tds[0].stripped_strings)[0]
            print(province)



