'''Static variables are as same in c++ but we also use them for Object '''
'''Lets Go towards code->>>>>>>>>>>>>>>>'''
class Employee:
    comp='Dell'
    no_emp=0
    def __init__(self,n):
        self.name=n
        Employee.no_emp+=1
    def show(self):
        print(f'{self.no_emp} {self.name} works in the company {self.comp}.')

obj1=Employee('Ali')
obj1.show()
obj2=Employee('Raza')
obj2.comp='Google'                          #We can also change the static variable in this way 
obj2.show()
obj3=Employee('Ishaq')
obj3.comp='HP'
obj3.show()