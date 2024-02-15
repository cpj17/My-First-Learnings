word=input('enter any word : ')
count=0
vws=''
for i in range(len(word)):
    ch=word[i]
    if(ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u'):
        count=count+1
        vws=vws+word[i]+' , '
print('totally',count,'words in',word,'\nthe words are :',vws[0:len(vws)-2])
