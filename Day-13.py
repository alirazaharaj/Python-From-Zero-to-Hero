# String are inmutable mean if we perform any action on them it will never change like 
# if we print a string into upper case latter main string will never change 
a='Hallo!!'
print(a.upper())
print(a.lower())
print(a)
# if we want to cut special charactors at the end of any(not last) string we use 
print(a.rstrip('!'))

print(a.replace('Hello','Boys'))

# capitalize() will turn first letter to upper case and other to lower case 
z='haLLo how are you BOYS'
print(z.capitalize())

# center() it will move string according to parameter givenn to them 
# if width of string is 25 and we gave 50 it will move string 25 from left side 
print(len(z))
print(z.center(50))
print(len(z.center(50)))

# we use to count that how many time the given worf came into the string 
print(z.count('a'))

# endwith tell that is the givem string end with that charactior 
print(z.endswith('S'))

# find will gave ocarance of first letter that given by the user 
print(z.find('BOYS'))

# isalnum() if the string consist on A-Z,a-z,0-9 htna it will return tru else false(even space) 
print(z.isalnum())

# isalpha() if the string consist on A-Z,a-z than it will return tru else false(even space) 
print(z.isalpha())

# islower() if the string consist on a-z than it will return tru else false(even space) 
print(z.islower())

# isprintable() will return true if given string will be printa ble not consist on \n\t\b tec 
print(z.isprintable())

# isspace() if the string consist on wide spacethan it will return tru else false 
print(z.isspace())

# istitle() if first letter string consist on upper letter it will return tru else false 
print(z.istitle())

# startswith() tell that the string start with given charactor
print(z.startswith('h'))

z='hallo how are you'
# swapcase() swap upper case letter to lower case and vise versa
print(z.swapcase())

# swapcase() comvert all starting charators of word into uper case
print(z.title())

