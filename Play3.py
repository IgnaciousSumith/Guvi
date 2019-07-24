a=int(input())
rev=0
while(a>0):
    f=a%10
    rev=rev*10+f
    a=a//10
print(rev)
