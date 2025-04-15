# def average(a,b):
#     print(a)
#     print(b)   # 'def' keyword is used to define a function 
#     return (a+b)/2

# print(average())    # It will give an error beacaue we did not pass any parameter

# Using Default Arguments
def average(a=10,b=20):
    print(a)
    print(b)   # 'def' keyword is used to define a function 
    print("The Average of two number is: ",(a+b)/2)

print(average(b=50))    #If we use any key value as a parameter so it will receive without parameter
