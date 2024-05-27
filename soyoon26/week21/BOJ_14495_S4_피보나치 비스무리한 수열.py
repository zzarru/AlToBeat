import sys
n = int(sys.stdin.readline().rstrip())
nums = [1,1,1] + [0]*n
for i in range(3,n):
    nums[i] = nums[i-1] + nums[i-3]
print(nums[n-1])