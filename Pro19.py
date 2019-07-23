a=int(input())
l=[]
for i in range (a):
    b=input()
    c=list(map(int,b.split()))
    l+=c
l.sort()
print(*l)
