import sys
def incoinspi (coinspi,b,Vd):
    if(Vd==0):
        return 0
    res=sys.maxsize
    for i in range (0,b):
        if(coinspi[i]<=Vd):
            sub_res= incoinspi(coinspi,b,Vd-coinspi[i])
            if(sub_res!=sys.maxsize and sub_res +1 < res):
                res=sub_res+1
    return res
n,Vd=list(map(int,input().split()))
coinspi=list(map(int,input().split()))
b=len(coinspi)
print(incoinspi(coinspi,b,Vd))
