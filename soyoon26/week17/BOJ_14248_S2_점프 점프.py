import sys
sys.setrecursionlimit(10**6)

n = int(input().rstrip())
v = [0]*(n+1)
bridge = list(map(int, sys.stdin.readline().split()))
s = int(sys.stdin.readline().rstrip())
cnt = 1
def dfs(x):
    global cnt
    for i in range(2):
        if not i:
            y = x+bridge[x]
        else:
            y = x-bridge[x]
        if 0<=y<n and not v[y]:
            v[y] = 1
            cnt += 1
            dfs(y)
dfs(s-1)
print(cnt)