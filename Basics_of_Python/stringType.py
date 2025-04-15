#Use string in python
s="I am Akshat Saxena"

print(s)
#Use multiline string in python
s1="""You are
the creator of your destiny"""
#Print the string
print(s1)
#print the string character by using index number.
print(s[7])
#Repitition of string in many times using * 
print(s1*10)

#Find the length of the string in the function in-built function
print(len(s1))

#Slicing in python
print(s1[0:25]) #we provide both starting and ending index of the string

print(s[0:])  #we provide only starting index

print(s[:12]) #we provide only ending index

print(s[-6:-1]) #It does include last right range index which is '-1' and it represets the last name of the string in negative slicing.
#Negative slicing is allowed in python.

print(s[0:10:2]) #it represents the one space gap in the string along with the index number

print(s[15::-1])
print(s[::-1])  #It is used to reverse the string.

#Remove unwanted space or white spaces using in python.
print(s.strip())
print(s.lstrip())

# More string methods

print(s.find('Aks',0,len(s))) #It is used to find the the occurence in the string.

print(s.replace("Akshat","Abhishek")) #This function is used for replace the string.
print(s.upper()) #Upper case character.
print(s.lower()) #Lower case character.



