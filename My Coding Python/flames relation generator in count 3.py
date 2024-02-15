count=3
f=list('FLAMES')
index=0
while len(f)>1:
    for i in range(count):
        index +=1
        print('index=',index)
        if index>len(f):
            print('in if')
            index=1
    f.remove(f[index-1])
    index -=1
    print(f)
print(f)
