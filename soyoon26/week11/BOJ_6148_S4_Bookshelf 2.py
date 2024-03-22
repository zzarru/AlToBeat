import sys
from itertools import combinations
N, B = map(int, sys.stdin.readline().split())
cows = [int(sys.stdin.readline().rstrip()) for _ in range(N)]

ans=[]
for i in range(1,N+1):
    lst = list(combinations(cows, i))
    for j in lst:
        if sum(j) >= B:
            ans.append(sum(j)-B)
print(min(ans))
