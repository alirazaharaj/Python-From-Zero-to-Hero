# if we use break statement than loop brake 
for i in range(1,12,1):
    if(i==11):
        print('Loop is destroyed........')
        break
    print('5 *',i,'=',i*5)


# if we use continue statement than one iteration of loop will be skip 
for i in range(1,12,1):
    if(i==11):
        print('Loop is destroyed........')
        continue
    print('5 *',i,'=',i*5)


# do while loop like structure 
# the given below structure runs atlest one time 
while(True):
    i=int(input('Enter a number: '))
    print('You enter ',i)
    if(i==5):
        break