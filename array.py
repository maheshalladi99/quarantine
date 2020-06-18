'''a=[1,2,3]
sum=0
for i in range(0,len(a)):
    for j in range(0,len(a)):
        #print("(",a[i],",",a[j],")")
        sum=sum+a[i]+a[j]
print(sum)

'''
import numpy
a=[11,11,22,33,33,44,44]
b=numpy.array(a)
print(b)
for i in range(0,len(a)):
    s=a.count(a[i])
    if(s==1):
        print(a[i])
    
