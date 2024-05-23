import sys, heapq
from collections import defaultdict
n=int(sys.stdin.readline().rstrip())
nums=[]
numd=defaultdict(int)
for _ in range(n):
    num = int(sys.stdin.readline().rstrip())
    numd[num] += 1
    if num < 0:
        heapq.heappush(nums,-num)
    elif num > 0:
        heapq.heappush(nums,num)
    else:
        if nums:
            np = heapq.heappop(nums)
            if numd[-np] > 0:
                numd[-np] -= 1
                print(-np)
            else:
                numd[np] -= 1
                print(np)
        else:
            print(0)
