# 'Tuple is a data structure which can not be modified(Immutable)'

tuple1=(10,20,30,40,10,20,40)
print(tuple1)
print(type(tuple1))

# if we take element in the tuple we write element with separate comma otherwise it treates as INT value 
# if we put single element in the tuple ex:-   tuple=(10,) must be write in the form of otherwise that will not be tuple that is integer
tpl=(10)
print(tpl)
print(type(tpl))

print(tuple1*3)
print(tuple1.count(50))   #It defines how many times element occures in the tuple.

lst=[10,20,90,'Akki']
print(lst)
print(type(lst))

tpl1=tuple(lst)
print(tpl1)
print(type(tpl1))