# if we want to import a ibrary 
'''
import math
print(math.cos(0))          '''

# Above statement will export all library if we want to export only some functions than we write 
'''
from math import pi,cos
print(cos(0)*pi)                           '''

# If we want that we gave some little or other name to the library we import than we use 
'''
import math as pd
print(pd.cos(0)*pd.pi*pd.sin(90))                       '''

# if we want to know that which built in functions present in library 
'''
import math
print(dir(math))                                       '''

# if we want that we import some piece of cord from our written file than 
from Day import a,b
print(a,'\n',b)