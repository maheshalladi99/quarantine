import numpy
l1=[]
i=1
while(i<=100):
    l1.append(i)
    #print(i,end=" ")
    i=i+1
    if(i%10==0):
        l1.append(i)
        #print(i,end=" ")
        for j in range(i+10,i,-1):
            #print(j,end=" ")
            l1.append(j)
        i=i+11
##ol=[]
##z=0
##d=0
##while(z<=10):
##    l=[]
ol=[]
m=0
n=10
for i in range(0,10):
    ol.append(l1[m:n])
    m=m+10
    n=n+10
##        if len(l)==10:
##            print(l)
##            break
##    d=k+10
##    ol.append(l)
    #z=z+1
#print(ol)        
ol.reverse()
ol=numpy.array(ol)
print("\n",ol)        
