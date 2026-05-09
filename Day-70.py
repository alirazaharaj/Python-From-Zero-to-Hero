# Is ma ham log aik data type sa dora data type ma jaya ga
# For this we use alternate constructure
# clas(string.split('-')[0],string.split('-')[1])
# Is line ma class return hogi .... 
# Us sa aga ya ana wali string ko spli kara ga un pieces ma jaha pa '-' laga hoga or pahla wala index ko pahla ma return kara ga or dosra wala ko dosra index ma return kara ga 
# Is mathod ko alternate constructure is lia kaha jata ha kio ka ya constructure ki tarah object ka constructure ko initialuze karn ka lia istimal hota ha 

class Employee:
    def __init__(obj,name,salary):
        obj.name=name
        obj.salary=salary
    def show(obj):
        print(f'{obj.name} has {obj.salary}$ salary.')
    @classmethod
    def changestr(clas,string):
        # ya easy code ha 
        # name,salary=string.split('-')
        # return clas(name,int(salary))
        return clas(string.split('-')[0],string.split('-')[1])

obj1=Employee.changestr('Ali-12000')
obj1.show()
