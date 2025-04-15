a=12 # Global Variable Declaration

def temp():
    a=36    # Local Variable declaration
    print(a)
    print(globals()['a'])

print(a)
c=temp #Assign Function to a variable
c()
c()
c()   
# print(locals()['a']) 