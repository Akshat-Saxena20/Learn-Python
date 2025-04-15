
list=[55,65.99,"Akshat Saxena",4,20]
print(list)

print(list[3])
print(list[0:3])
print(len(list))
print(list*3)

#Add or Remove the liat elements

list.append('Abhi')
list.append(18) #Add element in the list

list.remove('Akshat Saxena') #Remove the element of list
del(list[1])  #'del' is in-built function in python.
print(list)

# list.clear()
# print(list)

del(list[3])
print(list)
print(max(list)) #Max number of the list
print(min(list))  #min number of the list

list.insert(3,56)  #This function is used for insert an element at any position 'function parameters: index number,value.
print(list)

list.sort()     #This function is used for sort the list using python in-built function.
print(list)     #This function is sort element in ascending order.

list.sort(reverse=True)  #In sort function of python 'reverse keyword is used for sort the list in decending order order of boolean data type like 'True or 'False'.'
print(list)

list.sort(reverse=False)
print(list)