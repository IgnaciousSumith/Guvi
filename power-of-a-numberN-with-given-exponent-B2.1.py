def power(b,e ):
    if(e==1):
     return(b)
    if(e != 1):
     return(b*power(b,e-1))
b,e = map(int,(input().split()))
print(power(b,e))
