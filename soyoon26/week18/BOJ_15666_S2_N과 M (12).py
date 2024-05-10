import sys
n,m = map(int,sys.stdin.readline().split())
nums = list(set(map(int,sys.stdin.readline().split())))
nums.sort()
ans=[]
def back(start):
    if len(ans) == m:
        print(*ans)
        return
    for i in range(start,len(nums)):
        ans.append(nums[i])
        back(i)
        ans.pop()
back(0)