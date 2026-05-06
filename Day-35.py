# WE can use else statemnt with for loop 

for i in range(5):
    print(i)

else:
    print('Sorry i came into else block.......')


# when break statemnt break the loop than else condition will not run 
for i in range(5):
    print(i)
    if(i==4):
        break
else:
    print('Sorry i came into else block.......')
print('Sorry i came out from else block.......')


i=0
while(i<6):
    print(i)
    i=i+1
else:
    print('Sorry i came into else block.......')

i=0
while(i<6):
    print(i)
    i=i+1
    if(i==4):
        break
else:
    print('Sorry i came into else block.......')