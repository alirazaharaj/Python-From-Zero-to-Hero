# List concept
marks=[5,12,14,'Ali','Raza']

print(marks)

# Positive Indexing 
print(marks[0])

# Negative Indexing  
print(marks[-1])     #len(marks)-1///////// 5-1//////////print(marks[4])

# To check whether the given word present in the list we find using following method 
if 12 in marks:
    print('Yes')
else:
    print('No')


if 'Ali' in marks:
    print('Yes')
else:
    print('No')


if 'A' in 'Ali':
    print('Yes')
else:
    print('No')



# Jump idex 
# Increase index in a regulaar way 
print(marks[0:5:2])  #This list will increase with the increment of 2 men leave one value and print next


# Generate List on the time of print 
lis=[i for i in range(4)]
print(lis)

lis=[i*i for i in range(4)]      #It will print only number divible by 2
print(lis)

lis=[i*i for i in range(4) if i%2==0]      #It will print only number divible by 2
print(lis)

li=[i for i in range(1,11)]
lis=[item*5 for item in li ]
print(lis)
