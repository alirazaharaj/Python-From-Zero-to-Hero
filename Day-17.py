# Loops in python 

# for string 
name='ali raza'
for i in name:
    print(i)

# for list 
list1=['Red',[1,3],'Blue','White','Black']
for color in list1:
    print('\n',color,end=':')
    for i in color:
        print(i)

# for int 
for k in range(5):
    print(k)

for k in range(5):
    print(k+1)

# range(1,14) first is starting letter and ends with 14-1 
for k in range(1,14):
    print(k)
    if(k==5):
        print('is a Special charctor')
    elif(k==12):
        print(k,'is a Special charctor')
    elif(k==14):
        print(k,'is a Special charctor')

# range(1,10,2) loop start with first letter end at 10-1 and increment of third(2) one 
for k in range(1,10,2):
    print(k)