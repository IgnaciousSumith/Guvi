a,b=list(map(int,input().split()))
arr=list(map(int,input().split()))
c=[]
for i in range (b):
    d,e=list(map(int,input().split()))
    c.append(min(arr[d-1:e]))
for i in c:
    print(i)
