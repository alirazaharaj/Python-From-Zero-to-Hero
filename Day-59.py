# If we want that a specific syntax show on the start of a afunction than we use 'Decorator' 
def gret(fx):
    def mfx():
        print('Welcome to our program.........')
        fx()
        print('Thanks for using our program........')
    return mfx

@gret
def hallo():
    print('We are warmly welcome all of you to the knew classes of BSCS.')

hallo()


# Know if we want that we use parameters than we use 
def gret(fx):
    def mfx(*args,**kwargs):
        print('Welcome to our program.........')
        fx(*args,**kwargs)
        print('Thanks for using our program........')
    return mfx

@gret
def add(a,b):
    print(f'{a}+{b}={a+b}')

add(34,6)