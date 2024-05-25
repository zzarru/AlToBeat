import sys
sys.setrecursionlimit(10**9)
n,k=map(int,sys.stdin.readline().split())
graph=[[] for _ in range(n)]
for _ in range(n-1):
    u, v = map(int,sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)
apples=list(map(int,sys.stdin.readline().split()))
answer=0
visited=[False]*(n+1)
def dfs(v,cnt):
    global answer
    visited[v] = True
    if cnt <= k and apples[v]:
        answer+=1
    for i in graph[v]:
        if not visited[i]:
            dfs(i,cnt+1)

dfs(0,0)
print(answer)