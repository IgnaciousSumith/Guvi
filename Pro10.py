a=int(input())
b=list(map(int,input().split()))
c=0
for m in range (0,a):
    for p in range (0,m):
        if b[p]<b[m]:
            c=c+b[p]
print(c)
