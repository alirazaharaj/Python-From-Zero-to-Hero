'''In python there is nothing like other language like Private Protected and public 
Everrything in python oop is public 
Python dont restrict any member to use it private or protected but 
there are some convension we use to act data members as privet and protected 
But we also use them 
Lets Go to code Version     ------------->'''
class Student:
    def __init__(self):
        self.name='Ali'
        self.__age=20              # Protected Data member 
    def __show(self):
        print(f'{self.name} has {self.__age} years old.')

obj=Student()
print(obj.name)
# print(obj.__age)                 # We can not acess protected data member in this way 
print(obj._Student__age)           # But this was the convension for use to access the protected data member

obj._Student__show()               # To show protected function  