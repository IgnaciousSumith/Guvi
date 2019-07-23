from itertools import combinations
ab,x=map(int,input().split())
d=len(str(ab))
c=list(combinations(str(ab),d-x))
c=sorted(c)
print(*c[0],sep='')
