import random
comp=random.randint(1,3)
us=int(input('Enter 1)For Snake 2)For water 3)For Gun:   '))
def check(comp,user):
    if(comp==user):
        return 0
    elif(comp==1 and user==2):
        return -1
    elif(comp==2 and user==3):
        return -1
    elif(comp==3 and user==1):
        return -1
    else:
        return 1
wl=check(comp,us)
print(f'User: {us}')
print(f'Computer: {comp}')
if(wl==0):
    print('Match Draft...........')
elif(wl==1):
    print('You win the game.........')
else:
    print('You lose the game.........')