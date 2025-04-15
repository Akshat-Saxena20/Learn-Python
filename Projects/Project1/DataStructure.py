students={'Akshat':['Python','Django','Flask','DDN'],'Abhishek':['Java','Spring','JSP'],'Ajay':['JS','ReactJS','NodeJS'],'Savi':['php','LINUX','Pearl','Ruby']}
keys= students.keys()

for eachKey in keys:
    print("Cources taken by",eachKey," are: ")
    for eachCource in students[eachKey]:
        print(eachCource)

        