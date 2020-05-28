import numpy
import random
print("          welcome to the snakes and ladders game")
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

ol=[]
m=0
n=10
for i in range(0,10):
    ol.append(l1[m:n])
    m=m+10
    n=n+10

    
ol.reverse()
ol=numpy.array(ol)
#print("\n",ol)
#print(ol)

def movep1(p1,rv):
    p1=p1+rv
    #print("\nplayer",i,"at",p1)
    return p1
def movep2(p2,rv):
    p2=p2+rv
    #print("\nplayer",i,"at",p2)
    return p2
def movep3(p3,rv):
    p3=p3+rv
    #print("\nplayer",i,"at",p3)
    return p3
p1=1
p2=1
p3=1
d1=1
d2=1
d3=1
i1=int(input("\nPlayers count:"))
while((p1<100 and p2<100 and p3<100)):
    for i in range(1,i1+1):
        
        if i==1:
            print("\n\n{} PLATYER TURN\nPress enter:".format(i),end="")
            input()
            rv=random.randint(1,6)
            print("your value is:",rv)
            d1=movep1(p1,rv)
            p1=d1
            #print("\n\n","*********"*9,sep='')
            print("\n",ol)
            print("\nplayer",i,"at",p1)
            print("*********"*9)
        if i==2:
            print("\n\n{} PLATYER TURN\nPress enter:".format(i),end="")
            input()
            rv=random.randint(1,6)
            print("your value is:",rv)
            d2=movep2(p2,rv)
            p2=d2
            #print("\n\n","*********"*9,sep='')
            print("\n",ol)
            print("\nplayer",i,"at",p2)
            print("*********"*9)
        if i==3:
            print("\n\n{} PLATYER TURN\nPress enter:".format(i),end="")
            input()
            rv=random.randint(1,6)
            print("your value is:",rv)
            d3=movep3(p3,rv)
            p3=d3
            #print("\n\n","*********"*9,sep='')
            print("\n",ol)
            print("\nplayer",i,"at",p3)
            print("*********"*9)
        #print("player",i,"at",p1)
if(p1>p2 and p1>p3):
    print("player 1 is the winner")
if(p2>p1 and p2>p3):
    print("player 2 is the winner")
if(p3>p2 and p3>p1):
    print("player 3 is the winner")
