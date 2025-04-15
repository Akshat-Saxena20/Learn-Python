print()
print('Hello World!!')
print("All the power in with in you")

a,b=10,20
print(a,b,sep=(','))

name='Akshat'
marks=65.23
print("Name is ",name,"Marks is ",marks)

print("Name is %s,Marks is %.2f"%(name,marks))  # %.2f It prints only two points after the decimal point

#Specifiers in Python 
'''
    for integer value=%i
    for float value=%f
    for string value=%s
    for print the statements through the %(parameters)
'''

print("Name is {0}, Marks are {1}".format(name,marks))