# 爬取lol英雄的图片，ban、pick的音频文件
u = 'https://game.gtimg.cn/images/lol/act/img/js/heroList/hero_list.js'

import requests
import json

resp = requests.get(u);

# 获取接口数据   str
r = resp.content.decode('utf-8');
# print(r);

# 转为对象
dt = json.loads(r);
# print(dt); #dict   英雄信息在hero字段中

heros = dt['hero'];  # 所有的英雄  list

for h in heros:
    name = h['name'];  # 文件名
    en_name = h['alias'];  # 用来下载头像信息
    url_ban = h['banAudio'];  # 音频路径1
    url_pick = h['selectAudio'];  # 音频路径2

    dr = r"C:\Users\joker\Desktop\lol1";
    # 下载头像
    img = requests.get('https://game.gtimg.cn/images/lol/act/img/champion/{}.png'.format(en_name));
    f = open(dr + "\\" + name + ".jpg", 'wb');  # 图片，所以是b
    f.write(img.content);
    f.close();

    # 下载音频1
    ban = requests.get(url_ban);
    f = open(dr + "\\" + name + "_ban.ogg", 'wb');  # 音频，所以是b
    f.write(ban.content);
    f.close();

    # 下载音频2
    pick = requests.get(url_pick);
    f = open(dr + "\\" + name + "_pick.ogg", 'wb');  # 音频，所以是b
    f.write(pick.content);
    f.close();

    print("下载完毕:", name)