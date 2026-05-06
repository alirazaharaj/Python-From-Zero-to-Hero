# If we write a piece of code in which some error occur than remaining line will not run 
'''a=input('Enter a number: ')
for i in range(1,11):
    print(f'{int(a)} X {i} = {int(a)*i}')

print('\n\nWe put some inportant line of code here..........')
print('\n\n#############Thanks for using our program#############')          '''



# So if we want to run remaning line if some errror occur so we use following method
# >----But if try code run he will never run the except code 
a=input('Enter a number: ')
try:                                                    #it will try this piece of code
    for i in range(1,11):
        print(f'{int(a)} X {i} = {int(a)*i}')
except:                                                 #Otherwise he will run this piece of code
    print('Invalid Input Try Again........')








# To handel diff type of error 
try:
    a=int(input('Enter a number: '))
    b=[2,4]
    print(b[3])
except ValueError:
    print('Please enter a valid integer.....')

except IndexError:
    print('You enter a wrong Index..........')




print('\n\nWe put some inportant line of code here..........')
print('\n\n#############Thanks for using our program#############\n\n\n\n\n')  
