# Multiple order Inheritance 

class Employee:
    def __init__(self,name):
        self.name=name
    def show(self):
        print(f'Name of Employee:{self.name}')
    def arg(self):
        print('Hallo Employee class...........')
class Dancer:
    def __init__(self,dancer):
        self.dancer=dancer
    def show(self):
        print(f'Type of Danc:{self.dancer}')
    def arg(self):
        print('Hallo Dancer class...........')
class DancerEmployee(Employee,Dancer):
    def __init__(self, name,dancer):
        super().__init__(name)
        super().__init__(dancer)
    def arg(self):                                      #To call any parent class function
        Employee.arg(self)
        Dancer.arg(self)

'''In multiple inheritance we use order of class written in the braces and first compiler
    will see the code in
    Employeee class than into Dancer class '''

a=DancerEmployee('Shenda','Bar')
a.arg()