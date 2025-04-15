s='Saxena'
temp=[]
for c in s:
    if c not in temp:
        temp.append(c)
print(temp)

output=''.join(temp)
print(output)

