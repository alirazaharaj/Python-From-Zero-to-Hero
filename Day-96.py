'''asyncio--->>>>>>>Function use to call all function at same time or with delay of some second and functions will run paralllaly
    and no time of the compiler will be waste ..'''

import asyncio
import time
import requests

def fun1():
    print('First function.')
    time.sleep(2)
def fun2():
    print("Second function.")
    time.sleep(3)
def fun3():
    print("Third function.")
    time.sleep(4)

# To call all function at the same time we will use the following method
# This method is use when  a function take to much time and we want that there is no delay in the execution of any function given below

try:
    def main():
        asyncio.gather(
        fun1(),fun2(),fun3()
        )

    asyncio.run(main())
except:
    print('')
print('Hallo.........')
