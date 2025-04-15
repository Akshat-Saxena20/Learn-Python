lst=[20,30,40,50,60]
print(type(lst))

# b=bytes(lst)
# print(type(b))  #In the bytes we can not assign value with index number
# # b[3]=45

b = b'hello world'
print(b[0:5])  # Output: b'hello'


b1=bytearray(lst)
print(type(b1))
b1[4]=45        #In the byteArrays we can assign value with the index number

