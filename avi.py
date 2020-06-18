a=input().split( )
a1=int(a[len(a)-1])
for i in range(0,len(a[0])):
    print(a[0][a1],end='')
    a1=a1+1
    if a1==len(a[0]):
        a1=0
