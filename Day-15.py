# I import time
import time
# put time 
tim=time.strftime('%H:%M:%S')
print(tim)
tim=int(time.strftime('%H'))
if(tim<9)and(tim>11):
    print('Good Morning!........')
elif(tim>11)and(tim<14):
    print('Good After noon!........')
else:
    print('Good night')
