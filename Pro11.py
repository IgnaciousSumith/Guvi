a=int(input())
b=0
c=[]
for d in range (1,a+1):
    c.append(d)
for d in range (len(c)):
    for d in range (d+1,len(c)):
        b+=1
print(b)
