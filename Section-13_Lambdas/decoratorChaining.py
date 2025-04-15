# def square(fun):
#     def inner():



# def half(fun):
#     def inner():
#         n=fun()
#         return n/2
#     return inner




# def num():
#     return 15

# print(num())   
def square(fun):
    def inner():
        n=fun()
        return n*n
    return inner    




def half(fun):
    def inner():
        n=fun()
        return n/2
    return inner

@square
@half

def num():
    return 10








