start,end = map(int,(input().split()))
for n in range(start+1,end):
    x=0
    for i in range (2,n):
        if n%i==0:
            x=1
            break
        if x==0:
            print(n,end=" ")
