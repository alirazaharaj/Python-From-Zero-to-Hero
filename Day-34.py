dic={
    'ali':'Raza',
    'roll_no':'807',
    3:'waalikum',
    4:45
}
dic2={
    1:1122,
    2:33,
    3:4
}

# TO merge one dic into other 
dic.update(dic2)
print(dic)

# To delete all item in the dictionary
dic.clear()
print(dic)

# Make empty dictionary
dic={}
print(dic)

# To remove a key value pair we use 
dic2.pop(1)
print(dic2)

# To remove last key value we use
dic2.popitem()
print(dic2)

# To delete full dictionary we use 
del dic2
