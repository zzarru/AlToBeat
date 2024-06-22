import sys
t = int(sys.stdin.readline().rstrip())
for _ in range(t):
    nums = list(map(int,sys.stdin.readline().split()))
    nums.sort(reverse=True)
    print(nums[2])