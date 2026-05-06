Question=[
    ['Which languege is use in faceebook?','Java','C++','Python','none',4],
    ['Which languege is use in faceebook?','Java','C++','Python','none',4],
    ['Which languege is use in faceebook?','Java','C++','Python','none',4],
    ['Which languege is use in faceebook?','Java','C++','Python','none',4],
    ['Which languege is use in faceebook?','Java','C++','Python','none',4],
    ['Which languege is use in faceebook?','Java','C++','Python','none',4],
    ['Which languege is use in faceebook?','Java','C++','Python','none',4],
    ['Which languege is use in faceebook?','Java','C++','Python','none',4],
    ['Which languege is use in faceebook?','Java','C++','Python','none',4],
    ['Which languege is use in faceebook?','Java','C++','Python','none',4],
    ['Which languege is use in faceebook?','Java','C++','Python','none',4],
    ['Which languege is use in faceebook?','Java','C++','Python','none',4],
    ['Which languege is use in faceebook?','Java','C++','Python','none',4],
    ['Which languege is use in faceebook?','Java','C++','Python','none',4],
    ['Which languege is use in faceebook?','Java','C++','Python','none',4],
    ['Which languege is use in faceebook?','Java','C++','Python','none',4],
    ['Which languege is use in faceebook?','Java','C++','Python','none',4],
    ['Which languege is use in faceebook?','Java','C++','Python','none',4],
    ['Which languege is use in faceebook?','Java','C++','Python','none',4],
    ['Which languege is use in faceebook?','Java','C++','Python','none',4],
    ['Which languege is use in faceebook?','Java','C++','Python','none',4],
    ['Which languege is use in faceebook?','Java','C++','Python','none',4],
    ['Which languege is use in faceebook?','Java','C++','Python','none',4],
    ['Which languege is use in faceebook?','Java','C++','Python','none',4],
    ['Which languege is use in faceebook?','Java','C++','Python','none',4],
    ['Which languege is use in faceebook?','Java','C++','Python','none',4],
    ['Which languege is use in faceebook?','Java','C++','Python','none',4],
    ['Which languege is use in faceebook?','Java','C++','Python','none',4],
    ['Which languege is use in faceebook?','Java','C++','Python','none',4],
    ['Which languege is use in faceebook?','Java','C++','Python','none',4],
    ['Which languege is use in faceebook?','Java','C++','Python','none',4],
    ['Which languege is use in faceebook?','Java','C++','Python','none',4],
]

level=[1000,2000,3000,4000,1000,2000,3000,4000,1000,2000,3000,4000,1000,2000,3000,4000,1000,2000,3000,4000,1000,2000,3000,4000,1000,2000,3000,4000,1000,2000,3000,4000]
money=0

for i in range(0,len(Question)):
    qe=Question[i]
    print('\n\n\n\n\n\n',f'Question: {qe[0]}')
    print(f'a: {qe[1]}                       b: {qe[2]}')
    print(f'c: {qe[3]}                       d: {qe[4]}')
    try:
        a=int(input())
    except:
        print('Enter value b/w 1-4....')
        continue
    if(a==qe[5]):
        print(f'You gave correct ans,You have won {level[i]}$')
        if(i==4):
            money=10000
        elif(i==9):
            money=32000
        elif(i==14):
            money=1000000
        elif(i==32):
            money=10000000
    else:
        print('You gave wrong ans!!!')
        break

print('\n\n\n\n\n\n',f'You won the money from "KBC" is {money}$')

