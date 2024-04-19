import sys
from collections import defaultdict
n, k= map(int,sys.stdin.readline().split())
dolls = list(map(int,sys.stdin.readline().split()))
cnt=defaultdict(int)
start,end=0,0
ans=[]
while end<n+1:
    if cnt[1] >= k:
        ans.append(end-start)
        cnt[dolls[start]]-=1
        start+=1
    else:
        if end == n:
            break
        cnt[dolls[end]]+=1
        end += 1

if ans:
    print(min(ans))
else:
    print(-1)