name='Ali'
con='Pakistan'

# we can put variables into string using f-string 
c=f"\n\n\nMy name is {name}.I am from {con}."
print(c)


print(f"\n\n\nIf we print string as it is: \nMy name is {{name}}.I am from {{con}}.\n\n\n")



# wecan define number after floating deci mal using f-string method 
c=13.6784
print(f'Number after decimal {c:.2f}')

# if we want to change string 
c=f'{2*30}'
print(type(c),end='\n\n\n\n\n')