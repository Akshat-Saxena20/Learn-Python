# p=float(input("Enter the Marks of Pysics: "))
# c=float(input("Enter the Marks of Chemistry: "))
# m=float(input("Enter the Marks of Maths: "))

# if p>=35 and c>=35 and m>=35:
#     print("You have passed")
# avg=float(p+c+m)/3


# if avg<=59:
#     print("Grade 'C'")
# elif avg >59 and avg<=69:
#     print("Grade 'B'")
# elif avg >69 and avg <=100:
#     print("Grade 'A'") 
# else:
#     print("Fail")
                   
# print((35+35+35)/3)

m=float(input("Marks for Maths:"))
p=float(input("Marks for Physics:"))
c=float(input("Marks for Chemistry:"))

if m>=35 and p>=35 and c>=35:
    print ("You have passed!")

average= float((m+p+c)/3)

if average<=59: print("Grade is C")
elif average<=69: print("Grade is B")
else: print("Grade is A")

#else: print("You have failed!")