import os

# to form a folder 
'''
os.mkdir('OS-dir')              '''

'''
for i in range(1,101):
    os.mkdir(f'OS-dir/Day-{i}')             '''

# for update name 
'''
for i in range(1,101):
    os.rename(f'OS-dir/Day-{i}',f'OS-dir/Day-{i}.py')           '''

# To get list of folder present in any folder
fol=os.listdir('OS-dir')
print(fol)                                                         

# To find that in which directory am i working 
print(os.getcwd())

for fo in fol:
    print(fo)
    # to fimd folder with in folder 
    print(os.listdir(f'OS-dir/{fo}'))