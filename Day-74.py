# Method overidding 

class Rectangular:
    def __init__(self,l,w):
        self.l=l
        self.w=w
    def area(self):
        return self.l*self.w
class Circle(Rectangular):
    def __init__(self,r):
        super().__init__(r, r)
        self.r=r
    def area(self):
        return 3.14*super().area()

c=Circle(2)
print(c.area())