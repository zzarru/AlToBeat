import sys
n = int(sys.stdin.readline().rstrip())
nums = list(map(int,sys.stdin.readline().split()))
dp=[0]*n
for i in range(1, n):
    if nums[i-1] < nums[i]:
        dp[i] = dp[i-1] + 1
print(sum(dp)+n)