# Tuples are the collection of values which can  ot change 
tup=(1,2,3,'Harry',True)

# if we put only one value to tuple so we necessary put a comma at the end of that value 
tupl=(1,)

print(tup[0])
print(tup[2])
print(tup[-2])

# to check whether item present 
if True in tup:
    print('Yes present')


# slicing 
tup2=tup[2:4]
print(tup2)