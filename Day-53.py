# MAP 
l=[1,4,6,7,8,4,0,12]
# To apply any function on each value of a list we use map 
def sq(x):
    return x*x
new=list(map(sq,l))
print(new)
new=list(map(lambda x:x*x*x,l))
print(new)


# FILTER 
def re(x):
    return x>3
new=list(filter(re,l))
print(new)
new=list(filter(lambda x:x>=4,l))
print(new)

# REDUCE 
# we import reduce function 
from functools import reduce
new=reduce(lambda x,y:x+y,l)
print('The sum of l list is given as: ',new)