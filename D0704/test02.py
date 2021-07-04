'''
tuple1=['w','e','r','t',88,1]
print(len(tuple1))
print(max(tuple1))
print(min(tuple1))
print(max(tuple1))
'''


d = {"userName1":"豪","useAge":18,"userSal":123.46,"userName":"王伟"}

items = d.items()
for item in items:
    print(item)


keys=d.keys()
for s in keys:

    print("%s=%s"%(s,d[s]))