# import random
#
# arr = []
# while len(arr)!=20:
#     num = random.randint(1, 100)
#     if num not in arr:
#         arr.append(num)
# print(arr)
# arr.sort()
# print(arr[10:20])
# import random
# s = ""
# for i in range(100):
#     s += str(random.randint(0, 9))
# dirnum = {
#     "0": 0
# }
# for i in range(1, 10):
#     dirnum["%d" % i] = 0
# for i in s:
#     dirnum[i] += 1
#
# maxn = -1
# index = -1
# for i in range(0, 10):
#     if dirnum["%d"%i] > maxn:
#         maxn = dirnum["%d"%i]
#         index = i
#
# print("出现次数最多的数字为：", index)
# a=[[],[]]
# a[0].append()

global num
num = [1,2,4,6,13,12]
global goalMoney
goalMoney = [7, 15, 16]
tmp=[[1], [1,4], [0,4,22,33]]
curMoney=[0,0,0]
cur=0
for i in range(len(goalMoney)):
    print(i)
    print(len(goalMoney))
    print(curMoney[i],num[cur],goalMoney[i])
    if curMoney[i] + num[cur] <= goalMoney[i]:
        tmp[i].append(num[cur])
        curMoney[i] = curMoney + num[cur]
        curMoney[i] = curMoney[i] - num[cur]
        tmp[i].pop()