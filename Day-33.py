# Dictionary 
dic={
    'ali':'Raza',
    'roll_no':'807',
    3:'waalikum',
    4:45
}

print(dic)

# if we want to print some specific  value 
# if not present show error 
print(dic['ali'])

# if we want to print some specific  value 
# if not present show no error 
print(dic.get('wase'))


# if we want to access all keys 
print(dic.keys())

# if we want to access all values 
print(dic.values())

# loop 
for keys in dic:
    print(dic[keys])

for key in dic.values():
    print(f'The key is: {key} and value is {dic[keys]}')

# alahdakarna ka lia 
for key,values in dic.items():
    print(f'The key is: {key} and value is: {values}')