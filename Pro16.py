a=int(input())
list1=list(map(int,input().split()))
choco=1
count=0
if list1[0]>list1[1]:
    choco=choco+1
    count=count+choco
else:
    count=choco
for i in range (1,len(list1)):
    if list1[i]>list1[i-1]:
        choco=choco+1
        count=count+choco
    else:
        choco=1
        count=count+choco
print(count)
