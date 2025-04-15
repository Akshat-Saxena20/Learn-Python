dict={1:"Akki",2:"Abhi",3:"Vicky",4:"Priya",5:"Manas"}
print(dict)

print(dict.items())

k=dict.keys()       #Access the keys by using loop in dict
for i in k:print(i)

v=dict.values()     #Access the values by using loop in dict
for i in v:print(i)

print(dict[4])   #We can access dictionary by using 'keys number'

del dict[4]
print(dict)
