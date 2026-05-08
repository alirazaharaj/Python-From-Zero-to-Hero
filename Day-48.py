# Global variable is declair 
x=10
def a():
    x=3                #It will print 3 because its represent a local variable
    y=4
    print(x,'     ',y)

a()
print(x)   #It will print 10 because its a global variable 

def b():
    global x
    x=3                #It will print 10 because its represent now global variable
    global y
    y=4
    print(x,'     ',y)

b()
print(x,y)