# Generator
# It allow us to generate value while program is executed and values wil not stored in mameroy
import math
def my_gen():
    for i in range(6):
        yield i
def geno():
    for i in range(6):
        yield math.factorial(i)

gen=my_gen()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

obj=geno()
j=0
for i in obj:
    print(f'{j}!= ',i);j+=1

