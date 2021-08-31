#爬取b站排行榜
import requests
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36'
}
resp = requests.get("https://www.bilibili.com/v/popular/rank/douga?spm_id_from=333.851.b_62696c695f7265706f72745f646f756761.39",headers=header);
r = resp.content.decode("utf-8");
from bs4 import BeautifulSoup

ht = BeautifulSoup(r,'lxml');
la=ht.select('.content a.title')
print(len(la))
for a in la:
    print(a.get_text())
    print("https:"+a['href'])