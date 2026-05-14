'''Multiprocessing same ha threading ki tarah magar is ma aik sa ziada processor use hota ha jabka threading ma aik hi processor use hota ha '''

import multiprocessing
import multiprocessing.process
import requests

def download(url,name):
    print(f'Start Downloading {name}.....')

    response=requests.get(url)
    open(f'{name}.jpg','wb').write(response,)

    print(f'Finish Downloading {name}.....')

if __name__ == '__main__':
    url='https://picsum.photos/2000/3000'

    pros=[]

    for i in range (5):
        p=multiprocessing.Process(target=download,args=[url,i])
        p.start()
        pros.append(p)

    for p in pros:
        p.join()