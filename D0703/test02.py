n1=n2=n3=20

print(id(n3),n3)

n3=40
print(id(n3),n3)


a=1
sum=0
while a<=100 :
    sum+=a
    a+=1
print("1到100的和为"+str(sum))


a=0
while 1:
    account = input("input your acount:")
    if account == "admin":
        while a<3:
            password = input("input your password:")
            if password == '1234':
                print("Password is correct")
                break
            else:
                print("Password is error!")
                a+=1
        if a==3:
            print("Password is error three times!")
        break
