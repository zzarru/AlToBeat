import sys
sys.setrecursionlimit(10**9)
N=int(sys.stdin.readline().rstrip())
graph=[[] for i in range(N+1)]
for n in range(N-1):
    i,j=map(int,sys.stdin.readline().split())
    graph[i].append(j)
    graph[j].append(i)
visited=[False]*(N+1)
ans=dict()
def dfs(v):
    visited[v]=True
    for i in graph[v]:
        if not visited[i]:
            ans[i]=v
            dfs(i)
dfs(1)
for i in range(2,N+1):
    print(ans[i])