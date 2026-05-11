# Single Inheritance 

class Animal:
    def __init__(self,n):
        self.name=n
    def sound_made(self):
        print(f'Animal make sound')
class Dog(Animal):
    def __init__(self,n):
        super().__init__(n)
    def sound_made(self):
        super().sound_made()
        print('Bark!!!!!!!!!!!!!!!!!!!!')

d=Dog('D')
d.sound_made()
