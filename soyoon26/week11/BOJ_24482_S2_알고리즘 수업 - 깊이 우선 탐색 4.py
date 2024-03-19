import sys
sys.setrecursionlimit(10**6)
N,M,R=map(int,sys.stdin.readline().split())
graph=[[] for _ in range(N+1)]
for i in range(M):
    u,v=map(int,sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)
visited=[-1]*(N+1)

def dfs(v,cnt):
    visited[v]=cnt
    graph[v].sort(reverse=True)
    for i in graph[v]:
        if visited[i] == -1:
            dfs(i,cnt+1)

dfs(R,0)
print(*visited[1:],sep='\n')
