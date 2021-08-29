# # 爬取王者荣耀所有英雄头像
# # https://pvp.qq.com/web201605/herolist.shtml
#
# import requests  # 发起网络请求，得到响应内容
#
# from bs4 import BeautifulSoup  # 解析html页面，方便的找到想要的元素
#
# header = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36'
# }
# resp = requests.get("https://pvp.qq.com/web201605/herolist.shtml", headers=header);
# r = resp.content.decode("gbk");
#
# ht = BeautifulSoup(r, 'lxml');  # ht还是整个页面，不是列表
#
# imgs = ht.select('.herolist img');
#
# for img in imgs:
#     # 获取图片地址：
#     u = 'https:' + img['src'];  # src属性值
#     # 获取英雄名字
#     name = img['alt'];  # alt属性值
#
#     # 下载图片
#     resp = requests.get(u);
#     r = resp.content;
#     # 写文件
#     f = open(r'C:\Users\joker\Desktop\kings' + "\\" + name + ".jpg", 'wb');  # 注意路径，注意wb
#     f.write(r);
#     f.close();
#     print("已下载：", name);


#
# import requests
# header = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36'
# }
# resp = requests.get("https://www.bilibili.com/v/popular/rank/douga?spm_id_from=333.851.b_62696c695f7265706f72745f646f756761.39",headers=header);
# r = resp.content.decode("utf-8");
# from bs4 import BeautifulSoup
#
# ht = BeautifulSoup(r,'lxml');
# la=ht.select('.content a.title')
# print(len(la))
# for a in la:
#     print(a.get_text())
#     print("https:"+a['href'])
#
# import requests
# from bs4 import BeautifulSoup
# header = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36'
# }
# resp = requests.get("https://www.zanghaihua8.com/huozhou/345.html",headers=header);
# r = resp.content.decode("utf-8");
#
# ht = BeautifulSoup(r,'lxml');
#  #从ht中就可以找到我们想要的内容
#  #print(ht)
#  #找class=subject-item 里面的 h2 里面的a
#  #精准定位
# la = ht.select('.bookcontent')
# print(len(la))
# #print(la[0].get_text())
#
# f =open(r'C:\Users\joker\Desktop\test\小.txt','w');
# f.write(la[0].get_text())
# f.close()
# print("内容已下载：",r'C:\Users\joker\Desktop\test\小.txt')


from PIL import Image

im1 = Image.open(r"E:\图片\联想锁屏壁纸\8490181.jpg")
im2 = Image.open(r"E:\图片\联想锁屏壁纸\8500939.jpg")
print(im1.size)
print(im2.size)
print(im1.mode)
print(im2.mode)
im3 = Image.blend(im1, im2, 0.5)

#im3.show()

# from PIL import ImageEnhance
# bright = ImageEnhance.Brightness(im1).enhance(1.5)
# bright.show()
im1.thumbnail((200,200))
im2.paste(im1,(0,0))
im2.show()

