a=int(input())
b=0
for i in range (0,a):
    if(pow(2,i)>a):
        break
    b=a-pow(2,i)
print(b)
