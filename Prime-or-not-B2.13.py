c=int(input())
if((c<=10000)and (c>1)):
    for i in range (2,(c//2)+1):
        if((c%i==0)):
            print("No")
            break
        else:
         print("Yes")
