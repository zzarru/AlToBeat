import sys
n, m = map(int,sys.stdin.readline().split())
nums = list(map(int,sys.stdin.readline().split()))
nums.sort()
visited = [False]*n
ans=[]
def back(start):
    if len(ans) == m:
        print(*ans)
        return
    temp = 0
    for i in range(start,n):
        if visited[i] == False and temp != nums[i]:
            visited[i] = True
            ans.append(nums[i])
            temp = nums[i]
            back(i+1)
            visited[i] = False
            ans.pop()
back(0)