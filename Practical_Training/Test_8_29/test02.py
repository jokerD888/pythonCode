from PIL import Image
import random


# im = Image.new("RGB", (500, 500), (0, 0, 0))
#
# # for i in range(10):
# #     for j in range(10):
# #         im.paste((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
# #                  (j * 50, i * 50, (j + 1) * 50, (i + 1) * 50))
# #im.show()
# for i in range(500):
#     for j in range(500):
#         im.paste((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
#                  (j , i , j + 1, i + 1))
# im.show()

def setColor(img, blocksize):
    b = blocksize
    w, h = img.size
    for i in range(w // b):
        for j in range(h // b):
            img.paste((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
                      (j * blocksize, i * blocksize, (j + 1) * blocksize, (i + 1) * blocksize))


im = Image.new("RGB", (500, 500), (0, 0, 0))
setColor(im, 30)
im.show()
