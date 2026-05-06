# Raise an error by the programer 
# a=int(input('Enter a number b/w 5&9: '))
# if(a>10 or a<4):
#     raise  ValueError('Enter a correct Number.........')


a=input('Enter a quiet: ')
if(a!='quiet'):
    raise ValueError('Enter a valid string.........')