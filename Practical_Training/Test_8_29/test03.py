import tarfile

from PIL import Image
import random
import os  # 操作系统文件

dr = r"C:\Users\joker\Desktop\lol"
files = os.listdir(dr)  # 罗列出某个目录下的所有文件

files = list(filter(lambda x: ".jpg" in x, files))
filessize=len(files)
im = Image.new("RGB", (500, 500), (0, 0, 0))

for i in range(20):
    for j in range(20):
        #pic=Image.open(dr + '\\' + files[i * 10 + j]).resize((50, 50))
        im.paste(Image.open(dr + '\\' + files[random.randint(0,filessize-1)]).resize((25, 25)), (j * 25, i * 25))
im.save("E:\杂图\\test.jpg")
im.show()