# Doc string 
# A type of string that tell the programer about a function it was not a comment 
# It was written just below the function def 


def add():
    '''This will take value from user 
        and gave square'''
    a=int(input('Enter a number: '))
    print('Square of',a,'is',a*a)


add()

# out put of doc type 
print(add.__doc__)


# In given function it is not a doc type but its a comment 
# Because doc type is just below the function def 

def sq():
    a=int(input('Enter a number: '))
    '''This will take value from user 
        and gave square'''
    print('Square of',a,'is',a*a)

print(sq.__doc__)