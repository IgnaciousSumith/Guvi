a,b=map(str,input().split())
t=0
if len(a)>len(b):
    a,b=b,a
r=0
while r<len(a):
    t+=(ord(b[r]) - ord(a[r]))
    r+=1
for r in range (r,len(b)):
    t+=ord(b[r])-ord('c')+1
print(t)
    
