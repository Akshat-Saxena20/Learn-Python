
def Calculator(a,b):
    add=a+b
    subs=a-b
    mul=a*b
    div=a/b
    mod=a%b
    expo=a**b

    return add,subs,mul,div,mod,expo


a=int(input("Enter the value of a: "))
b=int(input("Enter the value of b: "))
result=Calculator(a,b)
for i in result:
    print(f"Result is : ",i)
