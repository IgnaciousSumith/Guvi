a,b=map(int,input().split())
c=[]
d=[]
c=input().split()
for e in range (len(c)):
    c[e]=int(c[e])
for e in range (b):
    f,g=map(int,input().split())
    res=0
    for e in range (f-1,g):
        res+=c[e]
    print(res)
