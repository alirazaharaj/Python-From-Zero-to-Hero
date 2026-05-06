# If we want taht a piece of code must run in every case so we use finally sattement
# a=input('Enter a number: ')
# try:                                                   
#     for i in range(1,11):
#         print(f'{int(a)} X {i} = {int(a)*i}')
# except:                                                 
#     print('Invalid Input Try Again........')
# finally:
#     print('I must execute...')


# WE know importance of this when we use all of this in function 
def we():
    a=input('Enter a number: ')
    try:                                                    
        for i in range(1,11):
            print(f'{int(a)} X {i} = {int(a)*i}')
            if(i==10):
                return 1
    except:                                                 
        print('Invalid Input Try Again........')
        return 0
    # In this case it will not run any code below return function so we use finally
    finally:
        print('I must execute...')

print(we())
