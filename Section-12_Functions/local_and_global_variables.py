# a=12 # Global Variable Declaration

# def temp():
#     a=36    # Local Variable declaration
#     print(a)

# print(a)
# temp();    


# Accesing the global variable in same name.

a=12 # Global Variable Declaration

def temp():
    a=36    # Local Variable declaration
    print(a)
    print(globals()['a'])

print(a)
temp();   
# print(locals()['a']) 