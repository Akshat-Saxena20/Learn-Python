a=[1,2,3,4]
b=[4,2,6,9]

c=[]
for i in a:
    if i in b:
        c.append(i)
print(c)   


c=[i for i in a if i in b]
print(c)
