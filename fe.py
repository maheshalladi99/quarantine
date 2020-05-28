import numpy
import random

print("\n\n                            *****welcome to the snakes and ladders game*****")

l1=[]
i=1

#creation of number

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

#rearanginig the number 

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


lad=["2 to 19","3 to 43","5 to 28 ","7 to 34","26 to 75", " 44 to 84 ", "39 to 99", "65 to 96"]


def ladder(d1):
    if(d1==2):
        print("\nPLAYER AT 2")
        print("he he ladder............ from 2 to 19")
        return 19
    if(d1==3):
        print("\nPLAYER AT 3")
        print("he he ladder............ladder from 3 to 43")
        return 43
##    if(d1==5):
##        print("\nPLAYER AT 5")
##        print("he he ladder............ladder from 5 to 77")
##        return 77
    if(d1==7):
        print("\nPLAYER AT 7")
        print("he he ladder............ladder from 7 to 34")
        return 34
##    if(d1==8):
##        print("\nPLAYER AT 8")
##        print("he he ladder............ladder from 8 to 28")
##        return 28
    if(d1==26):
        print("\nPLAYER AT 26")
        print("he he ladder............ladder from 26 to 75")
        return 75
    
    if(d1==39):
        print("\nPLAYER AT 39")
        print("he he ladder............ladder from 39 to 98")
        return 98
    if(d1==44):
        print("\nPLAYER AT 44")
        print("he he ladder............ladder from 44 to 84")
        return 84
    if(d1==65):
        print("\nPLAYER AT 65")
        print("he he ladder............ladder from 65 to 96")
        return 96
    else:
        return d1


snk=["99 to 2","91 to 10","76 to 26","46 to 15","72 to 2","37 to 14","80 to ","80 to 60"]


def snakes(d1):
    if(d1==99):
        print("\nPLAYER AT 99")
        print("oopsss snake bites you............ from 99 to 2")
        return 2
    if(d1==91):
        print("\nPLAYER AT 91")
        print("oopsss snake bites you............ from 91 to 10")
        return 10
    if(d1==76):
        print("\nPLAYER AT 76")
        print("oopsss snake bites you............ from 76 to 26")
        return 26
    if(d1==46):
        print("\nPLAYER AT 46")
        print("oopsss snake bites you............ from 46 to 15")
        return 15
    if(d1==72):
        print("\nPLAYER AT 72")
        print("oopsss snake bites you............ from 72 to 30")
        return 2
    if(d1==37):
        print("\nPLAYER AT 37")
        print("oopsss snake bites you............ from 37 to 14")
        return 14
    if(d1==80):
        print("\nPLAYER AT 37")
        print("oopsss snake bites you............ from 80 to 60")
        return 60
    else:
        return d1


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
            print("\n\n               ***********{} PLATYER TURN**********\n\nROLL YOUR DIE,(Press enter):".format(i),end="")
            input()
            rv=random.randint(1,6)
            print("your value is:",rv)
            d1=movep1(p1,rv)
            print("\n")
            d1=ladder(d1)
            d1=snakes(d1)
            p1=d1
            #print("\n\n","*********"*9,sep='')
            print("\n",ol)
            print("\nplayer",i,"at",p1)
            print("\n","The ladders are:--",lad)
            print("\n","The snakes are:---",snk)
            print("*********"*9)
            if(d1>=100):
                break

        if i==2:
            print("\n\n               ///////////{} PLATYER TURN/////////////\n\nROLL YOUR DIE,(Press enter):".format(i),end="")
            input()
            rv=random.randint(1,6)
            print("your value is:",rv)
            d2=movep2(p2,rv)
            d2=ladder(d2)
            d2=snakes(d2)
            p2=d2
            #print("\n\n","*********"*9,sep='')
            print("\n",ol)
            print("\nplayer",i,"at",p2)
            print("\n","The ladders are:--",lad)
            print("\n","The snakes are:---",snk)
            print("*********"*9)
            if(d2>=100):
                break

        if i==3:
            print("\n\n               &&&&&&&&&&&{} PLATYER TURN&&&&&&&&&&&&&&\n\nROLL YOUR DIE,(Press enter):".format(i),end="")
            input()
            rv=random.randint(1,6)
            print("your value is:",rv)
            d3=movep3(p3,rv)
            d3=ladder(d3)
            d3=snakes(d3)
            p3=d3
            #print("\n\n","*********"*9,sep='')
            print("\n",ol)
            print("\nplayer",i,"at",p3)
            print("\n","The ladders are:--",lad)
            print("\n","The snakes are:---",snk)
            print("*********"*9)
            if(d3>=100):
                break
        #print("player",i,"at",p1)


if(p1>p2 and p1>p3):
##    print("\U0001f600")
    print("......>>>>>>>>Player 1 is the winner>>>>>>>>>>>........")


if(p2>p1 and p2>p3):
    print("......>>>>>>>>Player 2 is the winner>>>>>>>>>>>........")


if(p3>p2 and p3>p1):
    print("......>>>>>>>>player 3 is the winner>>>>>>>>>>>........")
