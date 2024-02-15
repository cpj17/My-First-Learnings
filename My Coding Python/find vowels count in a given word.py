word=input('enter any word : ')
count=0
for i in range(len(word)):
    ch=word[i]
    if(ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u'):
        count=count+1
print('totally ',count,' words in ',word)
