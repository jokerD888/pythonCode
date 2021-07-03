n1=1.1
n2=2.2
print(n1+n2)
from decimal import Decimal
print(Decimal('1.1')+Decimal('2.2'))

print(type(n1))
print(str(n1),type(n1),type(str(n1)))
print(type(n1))

n=3
if n==3:
    print("zeze")
    print("yiyi")
else:
    print("haha")

account=input("input your acount:")
if account=="admin":
    password=input("input your password:")
    if password=='1234':
        print("Password is correct")