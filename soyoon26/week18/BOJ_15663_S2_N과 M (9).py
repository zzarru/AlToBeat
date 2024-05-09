import sys
n,m=map(int,sys.stdin.readline().split())
nums = list(map(int,sys.stdin.readline().split()))
nums.sort()
ans=[]
visited = [False] * n
def back():
    if len(ans) == m:
        print(*ans)
        return
    temp = 0
    for i in range(n):
        if not visited[i] and temp != nums[i]:
            visited[i] = True
            temp = nums[i]
            ans.append(nums[i])
            back()
            visited[i] = False
            ans.pop()
back()
