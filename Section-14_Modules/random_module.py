from random import *

# print(random()) # It takes a random value between (0-1) It takes normally floting value exclude 0 and 1

# for i in range(10):
#     print(randint(1,50)) # Print INT random number with including 1 and 50

# for i in range(10):
#     print(uniform(1,50))    #Print FLOAT random number with including 1 and 50


# for i in range(11):
#     print(randrange(1,20))

list=["Java","Javascript","Python","Django","Flask","tkinter","Flet","Numpy","pandas"]

for i in range(10):
    print(choice(list))