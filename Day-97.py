''''Thearding To use all given function at same time to reduce time consuption'''
import threading
import time
from concurrent.futures import ThreadPoolExecutor

def fun(sec):
    print(f'Function sleep for {sec}sec.')
    time.sleep(sec)
    return(sec)

def main():
    '''Normal Way '''
    ti1=time.perf_counter()
    fun(4)
    fun(3)
    fun(2)
    fun(1)
    print(time.perf_counter()-ti1)

    '''Using Threading'''
    ti1=time.perf_counter()
    t1=threading.Thread(target=fun,args=[4])
    t2=threading.Thread(target=fun,args=[3])
    t3=threading.Thread(target=fun,args=[2])
    t4=threading.Thread(target=fun,args=[1])

    # This will Just start the function 
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    # To stop any function when it complete we use below code but it may increase time 
    t1.join()
    print(time.perf_counter()-ti1)





'''>>>>>>More Convinient than above in real word '''
def polingdemo():
    with ThreadPoolExecutor() as executer:
        l=[4,3,2,1]
        result=executer.map(fun,l)
        # return will show here 
        for i in result:
            print(i)

polingdemo()