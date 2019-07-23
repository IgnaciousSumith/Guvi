import math
a,b=map(int,input().split())
c=[]
d=list(map(int,input().split()))
for i in range (0,b):
    e,f=map(int,input().split())
    c.append([e,f])
for i in c:
    g=i[0]-1
    h=i[1]-1
    print(math.gcd(d[g],d[h]))
