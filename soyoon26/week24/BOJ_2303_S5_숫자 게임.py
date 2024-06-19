import sys
from collections import defaultdict
from itertools import combinations
n = int(sys.stdin.readline().rstrip())
ans = defaultdict(int)
for i in range(n):
    nums = list(map(int,sys.stdin.readline().split()))
    candi = set(combinations(nums,3))
    max_n=0
    for j in candi:
        sum_n = str(sum(j))
        if int(sum_n[-1]) > max_n:
            max_n = int(sum_n[-1])
    ans[i+1] = max_n
value = max(list(ans.values()))
answer=0
for i,j in ans.items():
    if j == value:
        answer = i
print(answer)