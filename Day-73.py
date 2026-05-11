# Different method on the object of any class

from typing import Any


class Math:
    name='Ali Raza'
    def ___init__(self):
        self.name='Ali'
    def __str__(self):                                # Ya automatically call hojaya ga jab ap is class ka object ko print kara ga to
        return(f'Hallo my name is {self.name}.')
    def __repr__(self):                               #Agr oper wala method nahi hoga to ya call hoga 
        return(f'Hallo my name is {self.name}.I am calling repr method.')
    def __call__(self,a,b):                # Jab object ko funcion ka tor pa laga 
        return(print(f'The multiply of the given is {a*b}'))
obj=Math()
print(obj)
obj(3,4)
