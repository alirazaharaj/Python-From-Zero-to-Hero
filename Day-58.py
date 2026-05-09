# class
# ------------>Self yaha  pa as default use karna pada ga kio ka us objecty ko poimt karta ha 
class Student:
    # Constrauctor
    def __init__(self):
        self.name='--'
        self.roll_No=0
        self.clas='--'
    def get(self):
        self.name=input('Enter your name: ')
        self.roll_No=int(input('Enter your University Roll No: '))
        self.clas=input('Enter your class(BSCS-8): ')
    def show(self):
        print(f'{self.name} roll no {self.roll_No} class {self.clas}.')

a=Student()
b=Student()
a.get()
a.show()
b.show()