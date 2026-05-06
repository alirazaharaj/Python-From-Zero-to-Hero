import time
h=time.strftime('%H')
h=int(input('Enter hour: '))
if (h>0)and(h<12):
    print('Good Morning sir...........')
elif (h>=12)and(h<17):
    print('Good Afternoon sir...........')
elif (h>=17)and(h<=24):
    print('Good Night sir...........')
else:
    print('Enter a valid input............')

