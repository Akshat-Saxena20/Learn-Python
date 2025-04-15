class Product:
    def __init__(self):
        self.name="Samsung"
        self.description="Amazing Model"
        self.price=65000.15

    def display(self):
        print("The name of Mobile: ",self.name)
        print("The description about the phone is: ",self.description)
        print("Price of that phone is: ",self.price)    


p1=Product()
p1.display()    