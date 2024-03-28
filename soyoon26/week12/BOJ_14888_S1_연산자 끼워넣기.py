import sys
from itertools import permutations
N = int(sys.stdin.readline().rstrip())
num = list(map(int,sys.stdin.readline().split()))
cal = list(map(int,sys.stdin.readline().split()))
cal_num = []
for i in range(4):
    if i == 0:
        for j in range(cal[i]):
            cal_num.append(0)
    elif i == 1:
        for j in range(cal[i]):
            cal_num.append(1)
    elif i == 2:
        for j in range(cal[i]):
            cal_num.append(2)
    elif i == 3:
        for j in range(cal[i]):
            cal_num.append(3)

p_cal = list(permutations(list(cal_num),N-1))
answer=[]
for i in p_cal:
    ans = num[0]

    for k in range(N-1):
        if i[k] == 0:
            ans = ans + num[k+1]
        if i[k] == 1:
            ans = ans - num[k + 1]
        if i[k] == 2:
            ans = ans * num[k + 1]
        if i[k] == 3:
            ans = int(ans / num[k + 1])
    answer.append(ans)

print(max(answer),min(answer),sep='\n')





