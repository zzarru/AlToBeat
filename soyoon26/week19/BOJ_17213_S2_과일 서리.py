import math
n=int(input())
m=int(input())
nums=list(range(n))
ans=[]
answer=0
a = math.factorial(n+(m-n)-1)
b = math.factorial(m-n) * math.factorial(n-1)
print(a//b)