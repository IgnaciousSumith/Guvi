a=int(input())
fact=1
if(a==0):
    fact=1
else:
    for i in range (1,a+1):
        fact=fact*i
        print(fact)
