N,K= map(int,input().split())
arr = []
arr=[int(i) for i in input().split()]
i=0
sum=0
while K>0:
    sum +=arr[i]
    K=K-1
    i=i+1
print(sum)
