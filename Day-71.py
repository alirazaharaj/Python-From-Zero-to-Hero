# Different method 

# dir method is use to know all operation on the given string object list etc
a=['ali',2,'Raza']
print(dir(a))

# __dict__ use to tell the all values of object in the class
class Math:
    def __init__(self) -> None:
        self.name="Ali"
        self.roll=807
a=Math()
print('\n\n\n',a.__dict__,end='\n\n\n')


# help method is use to help proramer about a specific method 
print(help(Math))