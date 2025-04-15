class Patient:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        self.clinical=[]

    def addClinicalData(self,clincal):
        self.clinical.append(clincal)


class ClinicalData:


    def __init__(self,componentData,componentValue):
        self.componentData=componentData
        self.componentValue=componentValue


p = Patient("Akshat",18)
c1=ClinicalData('BP','80/180')
p.addClinicalData(c1)

c2=ClinicalData('heartRate',80)
p.addClinicalData(c2)

print(p.name)
for eachClinical in p.clinical:
    print(eachClinical.componentData)
    print(eachClinical.componentValue)

