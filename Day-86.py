# wirless operator
'''Operator that allow us to gave value of any 
    variable in the expression'''
a=True
print(a:=False)

num=[1,2,3,4,5]
while(n:=len(num))>0:
    print(num.pop())            #pop will cut last value fro the list

'''food=list()
while True:
    fo=input('Enter name of food: ')
    if fo=='quit':
        break
    food.append(fo)'''

# Above work can be don using Wirless operator
food=list()
while(fo:=input('Enter name of food: ')) !='quit' : food.append(fo)
print(food)

