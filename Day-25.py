'''we can ot change tupple directly first we will change it to list change it 
   than convert again into tupple 
'''
tup=('Pakistan','Iran','Saudia','Iraq','Nepal')
temp=list(tup)
temp.insert(2,'Turkey')
tup=tuple(temp)
print(tup)


# concatenate method 
temp=('India','Bangala','America')
temp2=tup+temp
print(temp2)

l=(1,3,4,2,1,777,1)

'''
To know how many time the given number are present in the list 
print(l.count(1))      '''




'''
To know that at which index the given number present we write      
print(l.index(4))
# To fine b/w some specific index we put initial index and final index 
print('The index of 777: ',l.index(777,2,6))              '''


# To find length of tupple 
print(len(l))