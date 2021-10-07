from operator import itemgetter
t,n,k=map(int,input().split())
i=0
trees=[]
for i in range(k):
    a=list(map(int,input().split()))
    a.append(a[0]+a[1]+a[3])
    trees.append(a)
trees=sorted(trees, key=(itemgetter(6)))
#print(trees)\
xo=0
yo=0
l=0
j=0
while(l<abs(trees[0][0]-xo)):
    #t-=1
    #if(t<0):
        #break
    if((trees[i][0]-xo)>0):
        print("move right")
    else:
        print("move left")
    l+=1
while(j<abs(trees[0][1]-yo)):
    t-=1
    if(t<0):
        break
    if((trees[i][1]-yo)>0):
        print("move up")
    else:
        print("move down")
    j+=1
xo=trees[0][0]
yo=trees[0][1]
t-=trees[0][3]
print("cut up")
