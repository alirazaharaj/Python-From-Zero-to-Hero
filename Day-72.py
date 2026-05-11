# Agr ham log super class ka koi function sub class ka kisi function ka under call karna chata ha to us ka lia ham super key word ka istimal kara ga 

class Employee:
    def __init__(self,name,id,city):
        self.name=name
        self.id=id
        self.city=city
    def show(a):
        print(f'{a.name} having id:{a.id} lives in {a.city}.')
class Officer(Employee):
    def __init__(self,name,id,city,scale):
        super().__init__(name,id,city)
        self.scale=scale
    def show(a):
        super().show()
        print(f'Having scale {a.scale}.')
a=Employee('Ali',807,'Jhang')
a.show()
b=Officer('Raza',802,'Jhang',19)
b.show() 