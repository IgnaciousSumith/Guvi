a=int(input())
b=list(map(int,input().split()))
b=[bin(i) for i in b]
b.sort(reverse=True)
b=[int(y,2) for y in b]
for i in range (0,a):
    print(b[i])
