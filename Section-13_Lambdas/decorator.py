def decorator(func):
    def inner():
        result= func()
        return result*2
    return inner

def number():
    return 55

resultfun=decorator(number)
print(resultfun())

