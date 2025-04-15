def fact(n):
    if n==0:
        result=1
    else:
        result=n*fact(n-1)
    return  result       

# result=fact(5)    
print("The factorial is: ",fact(5))  