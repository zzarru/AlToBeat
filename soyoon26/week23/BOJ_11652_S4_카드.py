import sys, heapq
from collections import defaultdict
n = int(sys.stdin.readline().rstrip())
nums = defaultdict(int)
for _ in range(n):
    num = int(sys.stdin.readline().rstrip())
    nums[num]+=1
sorted_nums = sorted(nums.items(), key=lambda x: (-x[1], x[0]))
print(sorted_nums[0][0])