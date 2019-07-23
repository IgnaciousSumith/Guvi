a,b=input().split()
c=abs(len(a)-len(b))
for i in range (len(a)):
    if len(b)==1 and b[i] in a:
        break
    if a[i] !=b[i]:
        c+=1
print(c)
