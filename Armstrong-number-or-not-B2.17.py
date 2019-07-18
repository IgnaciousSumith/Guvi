n= int(input(""))
n1=n
s=0
while n!=0:
    
    r=n%10
    s=s+r**3
    n=n//10
if s==n1:
    print("Yes")
else:
    print("No")
