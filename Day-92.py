"""Lru cache >>>>>>>>>>> LRU cache is a function or module that was use to store the numbers or an repeating data in the chche 
    agr hama pata ha ka ya program ziada time la raha ha or is ma values repeat ho rahi ha to ham us ma lru cache istimal kar la ga kio ka agr yo value pahla hi process ho chuki hogi to speedly process ho jaya gi 
    >>>>>>lakin agr values repeat na ho ya program ziada time na la to isa istimal na kijia ga """

from functools import lru_cache
import time
@lru_cache(maxsize=None)
def m(a):
    time.sleep(5)
    print(time.time())
    print(a)

print(m(2))
print(m(3))
print(m(4))
print(m(5))
print(m(7))

print(m(2))
print(m(3))
print(m(4))
print(m(5))
print(m(7))

print(m(10))