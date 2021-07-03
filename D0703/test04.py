
global account
account=0
global password
password=0
global balance
balance=0

#注册
def reg():I4
    print("--------------------------------------------------------")
    print("|                                                      |")
    print("|                    欢迎使用麾牌ATM机                  |")
    print("|                                                      |")
    print("--------------------------------------------------------")
    global account
    account=input("请输入您要注册的账号：")
    global password
    password=input("请输入您的密码：")


#登陆
def land():
    a=0
    while 1:
        id = input("请输入您的账号：")
        if id == account:
            while a<3:
                pwd = input("请输入您的密码：")
                if pwd == password:
                    print("密码正确，进入系统")
                    break
                else:
                    print("密码错误！")
                    pwd=input("请重新输入密码：")
                    a+=1
            if a==3:
                print("密码已输入3次，为保障您的财产安全，请明天再试！")
            break

#菜单
def menu():
    print("--------------------------------------------------------")
    print("|--------------------欢迎使用ATM机----------------------|")
    print("|         1.取款                      2.查询            | ")
    print("|         3.实时存款                  4.缴费            | ")
    print("|         5.转账                      6.退出            | ")
    print("--------------------------------------------------------")
    key=input("请输入您要使用的功能序号：")
    return key

#取款
def draw():
    global balance
    print("--------------------------------------------------------")
    print("                当前账户余额：%d元                 "%int(balance))
    print("                                                        ")
    getMoney=int(input("   请输入您要取款的数目："))
    print("   正在处理，请稍等......")

    if getMoney<balance:
        print("   余额不足，返回主界面")
    else:
        print("   取款成功，请注意查收")
        balance -= getMoney
    print("--------------------------------------------------------")
    #key=map()

#查询
def query():
    print("--------------------------------------------------------")
    print("   正在处理，请稍等......")
    print("--------------------------------------------------------")
    print("  当前账户：%s"%account)
    print("--------------------------------------------------------")
    print("                当前账户余额：%d 元                 "%int(balance))
    print("                1.返回                                  ")
    print("--------------------------------------------------------")
    key=input("请输入您要使用的功能序号：")
    while 1:
        if key!='1':
            key=input("序列号输入错误，请按照系统界面序列号再次输入：")
        else :
            break

#存款
def deposit():
    inputMoney=int(input("请输入存款金额："))
    print("--------------------------------------------------------")
    print("   正在处理，请稍等......")
    print("--------------------------------------------------------")
    global balance
    while 1:
        if inputMoney>0:
            balance+=inputMoney
            print("   交易成功！")
            print("--------------------------------------------------------")
            break
        else :
            inputMoney = input("输入金额有误，请重新输入：")
#缴费
def payPhone():

    key=input("      1.手机充值   0.返回")
    if key=='1':
        payMoney=int(input("请输入金额："))
        global balance
        while 1:
            if payMoney > 0:
                if balance > payMoney:
                    balance -= payMoney
                    balance-= payMoney
                    print("   交易成功！")
                    print("--------------------------------------------------------")
                    break
            else:
                payMoney = input("输入金额有误，请重新输入：")

#转帐
def transfer():
    dest=input("   请输入对方的账号：")
    key=input("    1.确定    2.退出")
    if key=='1':
        transMoney = int(input("请输入金额："))
        global balance
        while 1:
            if transMoney > 0:
                if balance>transMoney:
                    balance -= transMoney
                    print("   交易成功！")
                    print("--------------------------------------------------------")
                    break
                else:
                    print("余额不足！")
                    break
            else:
                transMoney = input("输入金额有误，请重新输入：")

reg()
land()
while 1:
    key=menu()
    if key=='1':
        key=draw()
    elif key=='2':
        key = query()
    elif key=='3':
        key = deposit()
    elif key=='4':
        key = payPhone()
    elif key=='5':
        key = transfer()
    elif key=='6':
        break

print("   退出成功，欢迎您再次使用麾哥牌ATM机   ")
print("--------------------------------------------------------")



