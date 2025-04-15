num=int(input("Enter a number: "))
pflag=True
for i in range(2,num-1):
    if num % i == 0:
        pflag=False
        break

if(pflag):
    print(num," is prime")
else:
    print(num," is not prime")        