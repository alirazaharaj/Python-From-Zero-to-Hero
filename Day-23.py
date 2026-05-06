l=[1,45,67,2,4,5,6]

# To add something at the end of list 
l.append(46)

# To resolve the list according to increasing order 
l.sort()

# To resolve the list according to Decreasing order 
l.sort(reverse=True)

'''
To reverse a list  
l.reverse()
'''

'''
To know that at which index the given number present we write 
print(l.index(4))
'''

'''
To know how many time the given number are present in the list 
print(l.count(1))
'''

'''
This mathod gave other name to one list but if we change one other will automatically change
m=l;m[0]='Ali';print(l)
'''

'''
But to copy a list we use copy() it will generate a new list
m=l.copy();m[0]='Raza';print(l,m)
'''

'''
if we want to add something i to list at specific idex than we sue 
l.insert(1,4444)     '''

'''
If we ant to add two lists 
m=['I','Love','Pakistan']
l=m+l                '''

print(l)