#Set

s={10,20,30,40,10,20}  # Set does not support duplicate values
print(type(s))
# Does not using index pattern
# Does not using slicing
# Can not perform repetition

# print(s[0])  # It gives an error during access element using index number
# print(s[0:5]) #Error in slicing
# print(s*3) #Error in repetition

s.update([33],[55])
print(s)

#Add and remove is allowed

s.remove(20)
print(s)
