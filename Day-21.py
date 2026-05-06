# defalt argument 
def add(a=1,b=0):
    print(a)
    print(b)
    print('Average:',(a+b)/2)
def name(a='ali',b='raza',c='haraj'):
    print(a,b,c)

add();add(2,2)
name();name('Sail','Raza','Haraj')

# change the order of argument 

add(b=6,a=2)


# tuple  
# if we dont know the length of number like 
def average(*num):
    sum=0
    for i in num:
        sum=sum+i
    print('\n\nsumof given numbers is ',sum/len(num))

# so we gave here how much number we want 
average(2,2)








# dictionary 
def name(**name):
    print('\n\n\nHello',name['n1'],name['n2'],name['n3'])

name(n1='Ali',n2='Ishaq',n3='Ahtasham')


