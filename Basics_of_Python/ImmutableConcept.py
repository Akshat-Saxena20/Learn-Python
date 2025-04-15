a=10
b=10

print(a is b)
print(id(a))
print(id(b))

x=True
y=True
print(x is y)
print(id(x))
print(id(y))

p="Akki"
q="Akki"
print(p is q)
print(id(p))
print(id(q))

#In python 'Immutable concept applies to every primitive dataType'
#If we assign same value of variable so both variables points to the same memory location which means python intreepiter saves the memory.