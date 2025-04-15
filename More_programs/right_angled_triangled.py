r=int(input('Enter the number of rows: '))
'''
for i in range(1,r+1):
    for j in range(1,i+1):  first way to print Right Angled Triangle
        print("* ",end="")

    print()    
'''
for i in range(1,r+1):
    print("* "*i)   # Second way to print Right Angled Triangle