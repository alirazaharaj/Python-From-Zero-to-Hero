'''Kaisa ham class/static variable ko change kar sakta ha'''


'''Self ya a object or @classmethod ma class ko represent karta ha '''


class MATH:
    comp='DELL'
    def show(a):
        print(f'{a.name} works in {a.comp}')
    #ya object ma change kara ga na ka class ka whole kara ga 
    def change(a,new):
        a.comp=new
    #ya ab whole class ma change kara ga 
    @classmethod
    def cha(a,na):
        a.comp=na

a = MATH()
a.name='Ali'
a.show()
a.change('Apple')
print('\n\nComany name till that time for whole class= ',MATH.comp)
a.cha('Google')
b=MATH()
b.name='Raza'
b.show()