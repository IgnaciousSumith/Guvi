a=int(input())
k=[]
for i in range (0,a):
    k.append(input())
b=len(k[0])
c=""
for i in range (0,b):
    d=k[0][i]
    f=0
    for j in range (0,a):
        if(d!=k[j][i]):
            f=1
    if(f==0):
        c=c+d
    else:
        break
print(c)
