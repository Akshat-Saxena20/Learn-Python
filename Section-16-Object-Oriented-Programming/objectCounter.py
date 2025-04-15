class ObjectCounter:

    no_of_objects=0

    def __init__(self):
        ObjectCounter.no_of_objects+=1

    @staticmethod
    def displayCount():
        print(ObjectCounter.no_of_objects)

o1=ObjectCounter()    
o2=ObjectCounter()
o3=ObjectCounter()    
o4=ObjectCounter()    
o5=ObjectCounter()    
o6=ObjectCounter()    
o7=ObjectCounter()    
o8=ObjectCounter()    
o9=ObjectCounter()    
o10=ObjectCounter()    
o11=ObjectCounter() 

# print(ObjectCounter.no_of_objects)
ObjectCounter.displayCount()

