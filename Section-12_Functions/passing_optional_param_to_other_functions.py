def myFun(x, *pos_param, **key_pos_param): # *args store the tuple
    # **kwargs stores the dictionary
    print(x)
    key_pos_param['id']=4370118
    for each_args in pos_param:
        print(each_args)
    for key,value in key_pos_param.items():
        print(key,value)
    modified_pos_param=pos_param+(50,)    
    my_Fun2(*modified_pos_param, **key_pos_param)    


def my_Fun2(*args, **kwargs):
    print(args)
    print(kwargs)        

myFun(10,20,30,'Akshat',name='Akshat',Class='SY BCS')            
