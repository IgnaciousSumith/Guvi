a,b=map(int,input().split())
l=[]
for _ in range (a):
    l.append(input())
for id in range (len(l)):
    if('0' in l[id]):
        l[id]=l[id].replace('0','')
    l[id]=l[id].replace('','')
lengths=[]
for id in l:
    if(len(id)>0):
        lengths.append(len(id))
b=min(lengths)
r='1'*b
r=r.strip()
for  id in range (b):
    print(r)
