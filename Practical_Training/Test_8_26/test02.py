
num = [2600, 41810, 2502, 13860, 5320, 7280, 18310, 3480, 13447, 1056, 3000, 51955, 28350, 5130, 3722, 12000
    , 7200, 1940, 14626, 3900, 22120, 20430]
goalMoney = [95990, 87843, 100205]
count_answer = 0

def GetAnswer(cur, tmp, curMoney):
    global count_answer
    if cur == len(num) or goalMoney == curMoney:
        if goalMoney == curMoney:
            count_answer = count_answer + 1
            print("方案", count_answer, ":")
            for i in range(len(tmp)):
                print("总金为：", goalMoney[i], "元的组成：")
                for j in range(len(tmp[i])):
                    print(tmp[i][j], end=" ")
                print()
#            exit(0)     #若要找出全部组合方案，注释此行代码即可
        return
    for i in range(len(goalMoney)):
        if curMoney[i] + num[cur] <= goalMoney[i]:
            tmp[i].append(num[cur])
            curMoney[i] = curMoney[i] + num[cur]
            GetAnswer(cur + 1, tmp, curMoney)
            curMoney[i] = curMoney[i] - num[cur]
            tmp[i].pop()

GetAnswer(0, [[], [], []], [0, 0, 0])
