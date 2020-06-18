while(1):
    a=int(input())
    b=list(map(int,input().split(" ")))
    print(b)
    d=set(b)
    c=list(d)
    
    if(len(b)!=len(c)):
        for i in range(len(c),len(b)):
            c.append(c[i-1]+1)
    co=0
    c.sort(reverse=1)
    print(c)
    for i in c:
        co=co+i
    print(co)

