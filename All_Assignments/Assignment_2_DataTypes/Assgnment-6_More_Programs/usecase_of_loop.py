n=int(input("Enter a number: "))

for i in range(1,n):
    if i % 10 == 0:
        if i > 100:
            break
        continue
    print(i)