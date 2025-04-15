class Teacher:

    def __init__(self,tname,desg,allocate_subject):
        self.tname=tname
        self.desg=desg
        self.allocate_subject=allocate_subject

    def outer_display(self):
        print("In outer Class")
        print("Teacher Name: ",self.tname)
        print("Designation: ",self.desg)
        print("Allocate Subject: ",self.allocate_subject)

    class student:
        def __init__(self,rollno,name,Class):
            self.rollno=rollno
            self.name=name
            self.Class=Class

        def inner_display(self):
            print("In inner Class")
            print("Student Rollno: ",self.rollno)    
            print("Student Name: ",self.name)    
            print("Student Class: ",self.Class)    

outer=Teacher("Akshada","HOD","Pysics")
# outer.outer_display()

inner=outer.student(1,"Akshat","SYBCA")

outer.outer_display()
inner.inner_display()

