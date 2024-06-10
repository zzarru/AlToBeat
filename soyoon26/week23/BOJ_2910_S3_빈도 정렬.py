import sys
from collections import defaultdict
n,c = map(int,sys.stdin.readline().split())
nums = list(map(int,sys.stdin.readline().split()))
cnt = defaultdict(int)
for i in nums:
    cnt[i]+=1
ans=list(cnt.values())
ans.sort(reverse=True)
for i in ans:
    for key,value in cnt.items():
        if i == value:
            for j in range(i):
                print(key,end=' ')
            del cnt[key]
            break