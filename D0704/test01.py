

'''money=1000  #余额
s=int(input("请输入取款金额："))  #取款金额
#判断余额是否充足
if money>=s:
    money-=s
    print("取款成功，余额为：",money)

num_a=int(input('请输入要比较的第一个数：'))
num_b=int(input('请输入要比较的第一个数：'))

print("使用条件表达式进行比较")
#print((num_a,'大于',num_b)  if num_a>num_b else (num_a,'小于',num_b))
print(str(num_a)+'大于'+str(num_b)  if num_a>num_b else str(num_a)+'小于'+str(num_b))
'''

print("%20s%20s%20s%20s"%("姓名","电话","QQ","邮箱"))

