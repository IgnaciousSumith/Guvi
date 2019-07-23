x,y=map(int,input().split())
l=list(map(int,input().split()))
for i in range (x):
    p,q =map(int,input().split())
    r=l[p-1:q]
    s=r[0]
    for i in range (1,len(r)):
        s=s^r[i]
    print(s)
