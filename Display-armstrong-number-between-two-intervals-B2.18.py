start,end=map(int,(input().split()))
for n in range (start,end):
    n1=n
    s=0
    while n!=0:
        r=n%10
        s=s+r**3
        n=n//10
    if s==n1:
      print(n1,end="")
 
