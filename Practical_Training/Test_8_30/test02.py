# 爬取lol英雄ban,select时的音频和头像
import requests
from bs4 import BeautifulSoup
import json

# 壳子，无法获取数据
# header = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36'
# }
# resp = requests.get("https://pvp.qq.com/web201605/herolist.shtml", headers=header)
# r = resp.content.decode("gbk")
# ht=BeautifulSoup(r,'lxml')
#
# la=ht.select(".clearfix a")
# print(len(la))

# 爬数据接口
u = "https://game.gtimg.cn/images/lol/act/img/js/heroList/hero_list.js"
resp = requests.get(u)
r = resp.content.decode("utf-8")

dt = json.loads(r)
dl = dt["hero"]
result = []
# print(dl)
for d in dl:
    name = d["name"]
    en_name = d["alias"]
    url_ban = d["banAudio"]
    url_pick = d["selectAudio"]

    dr = r"C:\Users\joker\Desktop\lol"
    # 下载头像
    img = requests.get("https://game.gtimg.cn/images/lol/act/img/champion/{}.png". format(en_name))
    f = open(dr + "\\" + name + ".jpg", "wb")
    f.write(img.content)
    f.close()

    # 下载ban音频
    ban = requests.get(url_ban)
    f = open(dr + "\\" + name + "_ban.ogg", "wb")
    f.write(ban.content)
    f.close()

    # 下载pick音频
    pick = requests.get(url_pick)
    f = open(dr + "\\" + name + "_pick.ogg", "wb")
    f.write(pick.content)
    f.close()

    print("下载完毕:",name)

