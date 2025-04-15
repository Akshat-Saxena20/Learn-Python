a=int(input("Enter the min value:"))
b=int(input("Enter the max value:"))

i=a
if i % 2 == 0: i=a+1
while i<=b:
    print(i)
    i+=2