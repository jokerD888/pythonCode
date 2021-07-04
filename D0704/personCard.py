
global name_list
name_list=[]
#菜单
def menu() :
    print("*******************************************")
    print("欢迎使用【名片管理系统】V 1.0")
    print()
    print("1.新增名片")
    print("2.显示全部")
    print("3.搜索名片")
    print()
    print("0.退出系统")
    print("*******************************************")
    answer=input("请选择希望执行的程序：")
    return answer

def add():
    print("您选择的操作是添加名片： ")
    print("--------------------------------------------")
    print("新增名片")
    name=input("请输入姓名：")
    phone=input("请输入电话：")
    QQ=input("请输入QQ：")
    mailbox=input("请输入邮箱：")
    d={"name":name,"phone":phone,"QQ":QQ,"email":mailbox }
    print("[{'name':'%s','phone':'%s','QQ':'%s','email':'%s'}]"%(name,phone,QQ,mailbox))
    print("添加%s的名片成功"%name)
    print("*******************************************")
    global name_list
    name_list.append(d)

def display():
    print("您选择的操作是显示名片： ")
    print("--------------------------------------------")
    print("显示所有名片")
    print("%-20s%-20s%-20s%-20s" % ("姓名", "电话", "QQ", "邮箱"))
    print("============================================")
    count=len(name_list)
    a=0
    while a<count:
        print("%-20s%-20s%-20s%-20s" % (
        name_list[a]["name"], name_list[a]["phone"], name_list[a]["QQ"], name_list[a]["email"]))
        a+=1
    print("*******************************************")

def search():
    print("您选择的操作是搜索名片： ")
    print("--------------------------------------------")
    print("搜索名片")
    searchName=input("请输入要搜索的名字")
    print("%-20s%-20s%-20s%-20s" % ("姓名", "电话", "QQ", "邮箱"))
    print("============================================")
    count = len(name_list)
    a = 0
    flag=False
    while a<count:
        if name_list[a]["name"]==searchName:
            print("%-20s%-20s%-20s%-20s" %(name_list[a]["name"], name_list[a]["phone"], name_list[a]["QQ"], name_list[a]["email"]))
            flag=True
        a+=1
    if flag:
        print("查询成功")
    else:
        print("查无此人")



while True:
    key=menu()
    if key=='1':
        add()
    elif key=='2':
        display()
    elif key=='3':
        search()
    elif key==0:
        break


