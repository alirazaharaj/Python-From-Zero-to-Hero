# Lambda function 

# lambda function act like a function but erite for one line 
avg=lambda x,y,z:(x+y+z)/3
print(avg(2,3,1))

# lambda function is use to pass a function as an argument in to other function 
def do(f,value):
    return 8*f(value)

# lambda function will act without any name 
print(do(lambda x:4*x,2))

