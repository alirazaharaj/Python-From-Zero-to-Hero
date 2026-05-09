class Library:
    def __init__(self):
        self.books=[]
        self.no=0
    def inp(self):
        self.books+=input('Enter Book: ')
        self.no+=1
    def show(self):
        print(f'Number of books={self.no}    Length={len(self.books)}')

obj=Library()
a=1
while (a==1):
    obj.inp()
    a=int(input('\n\n\nIf you want to input more books than enter 1 \nElse 0: '))

obj.show()