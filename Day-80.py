# Multilevel Inheritance 

class School:
    def __init__(self,name,id):
        self.name=name
        self.id=id
    def show(self):
        print(f'Name of school is \'{self.name}\' and Id \'{self.id}\'.')

class Teacher(School):
    def __init__(self, name, id,t_name):
        super().__init__(name, id)
        self.t_name=t_name
    def show(self):
        super().show()
        print(f'Name of Teacher is \'{self.t_name}\'.')

class Student(Teacher):
    def __init__(self, name, id,t_name,s_name,program):
        super().__init__(name, id,t_name)
        self.s_name=s_name
        self.program=program
    def show(self):
        super().show()
        print(f'Name of Student is \'{self.s_name}\'.\nStudying in {self.program}')

obj=Student('Govt Graduate College Jhang',3302,'Shazada','Xyz','BSCS')
obj.show()