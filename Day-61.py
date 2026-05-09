class Employee:
    def __init__(self):
        self.name=' '
        self.id=0
    def inp(self):
        self.name=input('Enter your name= ')
        self.id=int(input('Enter your id= '))
    def show(self):
        print(f'{self.name} with id {self.id}.')

class Language(Employee):
    def la(self):
        print('This man use Python language')

ab=['a1','a2','a3']
for i in ab:
    i=Employee()
    i.inp()
    i.show()

obj1=Language()
obj1.inp()
obj1.show()
obj1.la()