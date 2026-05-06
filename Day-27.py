lis_q=['When Pakistan win the word cup?','What was the name of the Capten when Pakistan win his first word cup?','Who hit logest six in the history of Word?','Who gave fastest ball in the history of word cricket?','What was the speed of fastest ball in yhe history of word cricket?']
lis_ans=['1998','Imran Khan','Shahid Afridi','Shoaib','63.3']
c=0
print('You have given five Question Ans them and Get Money...................')
i=0
while(i<=4):
    print('\n\n\n')
    s=input(lis_q[i])
    s=s.title()
    if(s==lis_ans[i]):
        c=c+1
    else:
        c=c
    i=i+1


print('\n\n\n\n\nCongraj You win money from KBC is',c*10000,end='$.')