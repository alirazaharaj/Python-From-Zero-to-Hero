# If we want to take than we use 
marks=[12,34,56,78,90,34,55,27]

for index,mark in enumerate(marks):
    print(mark)
    if(index==4):
        print('You don well effort my Boy.........')

# if we want that index start with 1 or other 
for index,mark in enumerate(marks,start=1):
    print(mark)
    if(index==4):
        print('You don well effort my Boy.........')

marks=['Ali','Hassan','Ishaq','Ahtasham','Zohaib','Samar']
for index,mark in enumerate(marks):
    print(mark)
    if(index==4):
        print('You don well effort my Boy.........')