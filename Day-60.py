class IO:
    def __init__(self):
        self.r=0
        self.sem=0
    def show(self):
        print(f'Roll No={self.r}   Semester={self.sem}')
# Getter Function --->>>>To show any value 
    @property
    def ten(self):
        return 10*self.r
# Setter Function --->>>>To set any value direct from program  
    @ten.setter
    def ten(self,a):
        self.r=a

obj=IO()

obj.r=10
print(obj.ten)
obj.show()