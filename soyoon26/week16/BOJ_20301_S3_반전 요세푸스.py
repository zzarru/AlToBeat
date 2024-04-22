import sys
from collections import deque
n,k,m=map(int,sys.stdin.readline().split())
nums = deque(range(1,n+1))
cnt=0
r=-k+1
while nums:
    if (cnt // m)%2:
        r=k
    else:
        r=-k+1
    nums.rotate(r)
    print(nums.popleft())
    cnt+=1