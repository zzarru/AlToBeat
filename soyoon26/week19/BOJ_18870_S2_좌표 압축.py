import sys
from collections import defaultdict
n = int(sys.stdin.readline().rstrip())
nums = list(map(int,sys.stdin.readline().split()))
nums_set=list(set(nums))
nums_set.sort()
nums_dict=defaultdict(int)
for i in range(len(nums_set)):
    nums_dict[nums_set[i]] = i
for i in nums:
    print(nums_dict[i],end=' ')


