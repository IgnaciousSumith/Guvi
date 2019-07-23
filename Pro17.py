a=input()
b=list(map(int,a.split()))
k=b[1]
h=input()
flag=0
s=list(map(int,h.split()))
for i in range (0,len(s)-1):
    for j in range (i+1,len(s)):
        if s[i]+s[j]==k:
            print("yes")
            flag=1
            break
    if flag==1:
        break
if flag!=1:
    print("no")
