# Time module 
import time

# Time.time tell the time in second from 1979 i think

i=time.time()
print(i)
print(time.time()-i)

# Sleep time is ma value second ma hogi

time.sleep(2)
print(time.time())

# It tell the local time and formate tell the formate of time

i=time.localtime()
f=time.strftime('%d/%m/%Y =>%H:%M:%S',i)
print(f)