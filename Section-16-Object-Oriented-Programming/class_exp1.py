class Course:
    
    def __init__(self, name, ratings):  # self points to the current object being created
        self.name = name        # creates instance variable name
        self.ratings = ratings  # creates instance variable ratings
    
    def Avg(self):
        numberofRatings = len(self.ratings)  # self.ratings accesses instance variable
        Average = sum(self.ratings)/numberofRatings
        print("The Average ratings for", self.name, "is: ", Average)

c1=Course("AWS course",[1,2,3,4,5]) 
print(c1.name)
print(c1.ratings)
c1.Avg()       
    

c2=Course("JAVA course",[5,5,5,5,5]) 
print(c2.name)
print(c2.ratings)
c2.Avg()



c3=Course("Python Course",[4,3,3,5,5]) 
print(c3.name)
print(c3.ratings)
c3.Avg()

    