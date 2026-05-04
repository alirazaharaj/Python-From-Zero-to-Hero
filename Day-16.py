# switch case like statement 

a=int(input('Enter a value: '))
match a:
    case 1:
        print('Given num is one')
    case 2:
        print('Given num is two')
# default statement 
    case _:
        print('Given num is: ',a)

b=int(input('Enter a value: '))
match b:
    case 1:
        print('Given num is one')
    case 2:
        print('Given num is two')
# default statement 
    case _ if(b>9):
        print('Given num is greater than 9')
    case _ if(b==9):
        print('Given num is equal to 9')
    case _:
        print('Given num is: ',b)
