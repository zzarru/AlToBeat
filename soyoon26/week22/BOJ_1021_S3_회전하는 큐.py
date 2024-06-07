import sys
from collections import deque
n, m = map(int,sys.stdin.readline().split())
pick = list(map(int,sys.stdin.readline().split()))
nums = deque(range(1,n+1))
answer=0
for i in pick:
    while nums[0] != i:
        x = nums.index(i)
        if len(nums)-x > x:
            nums.rotate(-x)
            answer+=x
        else:
            nums.rotate(len(nums)-x)
            answer+=len(nums)-x
    nums.popleft()
print(answer)