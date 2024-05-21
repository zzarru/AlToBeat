import sys
import heapq
n = int(sys.stdin.readline().rstrip())
nums = []
for _ in range(n):
    num = list(map(int,sys.stdin.readline().split()))
    for i in num:
        if len(nums) < n:
            heapq.heappush(nums,i)
        else:
            if nums[0] < i:
                heapq.heappop(nums)
                heapq.heappush(nums,i)
print(nums[0])


