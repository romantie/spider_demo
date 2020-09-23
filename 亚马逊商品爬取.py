import requests
try:
    kv = {'user-agent': 'Mozilla/5.0'}
    url ="https://www.amazon.cn/dp/B078FFX8B6/ref=cngwdyfloorv2_recs_0/459-0245372-6102030?pf_rd_m=A1AJ19PSB66TGU&pf_rd_s=desktop-2&pf_rd_r=MM3MMK9E2VA4DJNSKB3S&pf_rd_r=MM3MMK9E2VA4DJNSKB3S&pf_rd_t=36701&pf_rd_p=d0690322-dfc8-4e93-ac2c-8e2eeacbc49e&pf_rd_p=d0690322-dfc8-4e93-ac2c-8e2eeacbc49e&pf_rd_i=desktop"
    r = requests.get(url,headers = kv)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text[1000:2000])
except:
    print("产生异常")
