class Programmer:
    def setName(self,n):
        self.name=n

    def getName(self):
        return self.name

    def setSalary(self,sal):
        self.salary=sal

    def getSalary(self):
        return self.salary

    def setTechnology(self,tech):
        self.technology=tech

    def getTechnology(self):
        return self.technology
    
print("The Details of First Programmer")
print("---------------------------------------------")

p1=Programmer()
p1.setName("Akshat Saxena")
p1.setSalary(45000)
p1.setTechnology(["C","C++","Python","Numpy","Pandas","Flet","Javascript"])

print("The name of programmer is: ",p1.getName())
print("The salary of first programmer is: ",p1.getSalary())
print("The technology who have: ",p1.getTechnology())



print("The Details of Second Programmer")
print("---------------------------------------------")

p2=Programmer()
p2.setName("Abhishek Saxena")
p2.setSalary(97000)
p2.setTechnology(["C","C++","Python","Django","Flask","Docker","Kubernetes","Jenkinns","CI/CD","BASH"])

print("The name of programmer is: ",p2.getName())
print("The salary of second programmer is: ",p2.getSalary())
print("The technology who have: ",p2.getTechnology())



print("The Details of Third Programmer")
print("---------------------------------------------")

p3=Programmer()
p3.setName("Srishti Saxena")
p3.setSalary(81000.45)
p3.setTechnology(["C","C++","Java","Javascript","CSS","HTML","OS"])

print("The name of programmer is: ",p3.getName())
print("The salary of third programmer is: ",p3.getSalary())
print("The technology who have: ",p3.getTechnology())



# p2=Programmer("Abhishek Saxena",85000.45,"DevOps")
# print(p2.name)
# print(p2.salary)
# print(p2.technology)


# p3=Programmer("Srishti Saxena",75000,"Java")
# print(p3.name)
# print(p3.salary)
# print(p3.technology)


            