def reverse(s): 
  str = "" 
  for i in s: 
    str = i + str
  return str
s=str(input())
print(reverse(s))
