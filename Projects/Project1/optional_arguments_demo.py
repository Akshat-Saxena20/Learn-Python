def myFun(x, *args, **kwargs): # *args store the tuple
    # **kwargs stores the dictionary
    print(x)
    for each_args in args:
        print(each_args)
    for key,value in kwargs.items():
        print(key,value)

myFun(10,20,30,'Akshat',name='Akshat',Class='SY BCS')            


def myFun(x, *pos_param, **key_pos_param): # *args store the tuple
    # **kwargs stores the dictionary
    print(x)
    for each_args in pos_param:
        print(each_args)
    for key,value in key_pos_param.items():
        print(key,value)

myFun(10,20,30,'Akshat',name='Akshat',Class='SY BCS')            