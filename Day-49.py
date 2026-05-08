
# 'r' for read only and by default 'w' for write and many other method 'rb for binary  file '
'''
f=open('tp.txt','r')
f=f.read()
print(f)                '''

# to write we use =>>>>But it will erase all present data
''' 
f=open('tp.txt','w')
f=f.write('Hallo Ali how are you......')                        '''

# to append we use =>>>>But it will not erase present data
f=open('tp.txt','a')
f=f.write('\n\Hallo Ali how are you......\n') 

with open('tp.txt','a') as f:
    f.write('I come..........\n\n')