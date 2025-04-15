# First Way to Product of two lists
x=[1,2,3,4,5]
y=[9,8,7,6,5]
z=[]

for i in range(len(y)):
    z.append(x[i]*y[i])
print(z)    

# Second way to Product of two lists using List Comprehension

z = [x[i] * y[i] for i in range(len(x))]
print(z)