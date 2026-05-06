cd=int(input('Enter 1 for coding enter 2 for decoding: '))
out=''
if(cd==1):
    inp=input('Enter word you want to code: ')
    if(len(inp)<=3):
        inp=inp[1:]+inp[0]
        out='abc'+inp+'def'
    else:
        out=inp[::-1]
    print(out)
elif(cd==2):
    inp=input('Enter word you want to decode: ')
    if(len(inp)<=3):
        out=inp[::-1]
    elif((inp[0]=='a')and(inp[1]=='b')and(inp[2]=='c')):
        out=''
        i=inp[3:-3]
        out=i[::-1]
    else:
        out=inp[::-1]
    print(out)