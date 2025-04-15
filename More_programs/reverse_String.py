s=input('Enter a string: ')
print(s[::-1])   # Using Slicing

i=len(s)-1      # Using custom approach
result=''
while i>=0:
    result=result+s[i]
    i=i-1
print(result)    