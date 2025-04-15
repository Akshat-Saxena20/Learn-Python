class Product:
    def __init__(self):
        self.name="Samsung"
        self.description="Amazing Model"
        self.price=65000.15

    def __del__(self):
        print("Inside the destructor")

    def display(self):
        print(self.name)
        print(self.description)
        print(self.price)    


p1=Product()
p1.display()
p1=None

p2=Product()
p2.display()
p2=None
# print(p1.name)
# print(p1.description)
# print(p1.price)        