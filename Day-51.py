f=open('tp.txt','r')

# It will move the reader at given point and consider in bite 
'''f.seek(5)'''

# Tell that at which position cursor will present 
'''print(f.tell())'''

# it will print tha ramaning data 
'''
data=f.read(5)
data=f.read()            # =>>>>Both values are correct 
print(data)'''

f=open('tp.txt','w')
f.write('Hallo word...')
f.truncate(5)               #It will allow to write only given charactors in the file 

f=open('tp.txt','r')
f=f.read()
print(f)