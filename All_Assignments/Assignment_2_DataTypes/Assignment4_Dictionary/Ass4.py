
student_info={"name":"Akshat","Age":12,"Major":"Yes"}

print(student_info)
print(type(student_info))

print(student_info["name"])
print(student_info["Age"])

student_info.update({"email":"akshat@gmail.com"})
print(student_info)

student_info["Age"]=18
print(student_info)

del student_info["Major"]
print(student_info)