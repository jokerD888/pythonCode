def jishu(x):
    if x%2 :
        print("%d是奇数"%x)
    else :
        print("%d是偶数"%x)

jishu(3)
from decimal import Decimal
def getMax(a,b,c):
    n1=n2=n3=a
    if b>n1:
        n1=b
    if c>n1:
        n1=c
    if b<n3:
        n3=b
    if c<n3:
        n3=c

    #n2=Decimal('a') + Decimal('b')+Decimal('c') - Decimal('n1') - Decimal('n3')
    n2=a+b+c-n1-n3
    #n2=Decimal('n2')
    print(n3,n2,n1)

a=input("输入第一个数")
b=input("输入第二个数")
c=input("输入第三个数")
if  '.' in a:
    a=float(a)
else:
    a=int(a)
if  '.' in b:
    b=float(b)
else:
    b=int(b)
if  '.' in c:
    c=float(c)
else:
    c=int(c)
getMax(a,b,c)