for j in range(40):
    count=j+1
    f=list('FLAMES')
    index=0
    while len(f)>1:
        for i in range(count):
            index +=1
            if index>len(f):
                index=1
        f.remove(f[index-1])
        index -=1
    print(j+1,' = ',f)
