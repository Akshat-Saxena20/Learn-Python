import mymath as m  
# In this module we have to create a file 'mymath.py' then i have import 
# mymath module in this file 
# 'mymath.py all the function of calculator'

#In this module only import

print(m.Add(25,25))
print(m.Subtract(20,10))

print("---------------------------------------------------------------")

# In this block of code all the functions import from mymath.
# Which is given in 'mymath.py'
from mymath import *
print(Add(20,30))
print(Subtract(50,20))
print(Multiply(50,5))
