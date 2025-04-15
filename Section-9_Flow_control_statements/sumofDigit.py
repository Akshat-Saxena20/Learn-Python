num=int(input("Enter the value of n: "))
sod=0
while num>0:
    rem=num%10
    sod=sod+rem
    num=num//10

print("Sum of Digits is: ",int(sod))
