import sys
n,m = map(int,sys.stdin.readline().split())
nums = list(map(int,sys.stdin.readline().split()))
nums.sort()
ans=[]

def back():
    if len(ans) == m:
        print(*ans)
        return
    for i in nums:
        ans.append(i)
        back()
        ans.pop()
back()