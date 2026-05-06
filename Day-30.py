# Recursion:Calling of function in itself 

def fac(i):
    if (i==0)or(i==1):
        return 1
    else:
        return i*fac(i-1)


n=int(input('Enter number whose factorial you want to know: '))
print(fac(n))



# Femonachi series 
def fn(n):
    if (n==0):
        return 0
    elif(n==1):
        return 1
    else:
        return fn(n-1)+fn(n-2)

n=int(input('Enter number whose fabconic you want to know: '))
print(fn(n))


