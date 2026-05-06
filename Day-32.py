s={1,3,2,4,4,6,2,3,'ali'}
v={40,50,3,1,'ali','raza'}

# Same as methematics 
print(s.union(v))

# take same vlue from both sets 
print(s.intersection(v))

# take value from v that are not present in s add vlues to v 
v.update(s)
print('update',v)

# To take values which are present in s but not in v 
z=s.symmetric_difference(v)
print(z)

# Is-disjoint : set which have no same value 
s={1,2,'ali'}
v={5,3,'raza'}
print(s.isdisjoint(v))


# Sper set:set which have all item of other set 
s={1,2,'ali',5,3,'raza'}
v={5,3,'raza'}
print(s.issuperset(v))

# sub set:
print(v.issubset(s))

# if you want to add one item to set 
s.add("How are you")
print(s)

# if you remove something from set 
s.remove("How are you")
print(s)

# Discard pkay same roll as remove but if we put wrong value than it will not rase error 
s.discard(5)
s.discard(1111)
print(s)

# pop will return first item of that set 
print('Pop:......',s.pop())

# del will delete whole set 
q={1.,3,4,5}
del q          # it will show error if we print q ->>>>>>>>>>>>>> print(q)


# clear will delete whole item in the set
q={1,2,3,4,5,6}
q.clear()
print(q)




# using if condition 
v={40,50,3,1,'ali','raza'}
if 'ali' in v:
    print('Yes it is present...')
else:
    print('It is not present...')