import math
n = int(input())
num = math.factorial(n)
num = str(num)
for i in range(len(num)-1,-1,-1):
    if num[i] != '0':
        print(num[i])
        break
