import os
files=os.listdir('pic')
i=1 
for file in files:
    if file.endswith('.png'):
        os.rename(f'pic/{file}',f'pic/{i}.png')
        print(file)
        i+=1
