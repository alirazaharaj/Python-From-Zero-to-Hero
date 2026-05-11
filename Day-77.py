# Operator Overloading

class Vector:
    def __init__(self,i,j,k):
        self.i=i
        self.j=j
        self.k=k
    def __str__(self):
        return f'{self.i}i + {self.j}j + {self.k}k'
    def __add__(self,x):
        #If we dont use vector than data type will be string so we use vector 
        return Vector(self.i+x.i,self.j+x.j,self.k+x.k)

a=Vector(4,5,12)
print(a)
b=Vector(1,7,2)
print(b)
print(a+b)
print(type(a+b))