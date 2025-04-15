def decor(fun):
    def inner(n):
        result=fun(n)
        result+=" How are you?"
        return result
    return inner


@decor
def hello(name):
    return "Hello " +name
print(hello("Akshat"))