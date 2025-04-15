# Nested Function

def display(name):
    def message():
        return "Hello, "
    result=message()+name
    return result

print(display("This is Akshat Saxena"))    