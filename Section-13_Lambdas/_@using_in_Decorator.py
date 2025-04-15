def decorator(func):
    def inner():
        result= func()
        return result*2
    return inner

@decorator
def number():
    return 55

print(number())


