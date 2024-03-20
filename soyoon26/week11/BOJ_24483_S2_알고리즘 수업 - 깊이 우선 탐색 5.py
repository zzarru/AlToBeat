import sys #깊이와 방문순서
sys.setrecursionlimit(10**9)
N,M,R = map(int,sys.stdin.readline().split())
graph=[[] for _ in range(N+1)]
visited=[-1]*(N+1)
for i in range(M):
    u,v=map(int,sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)
answer=0
cnt=0
def dfs(v,d):
    global answer,cnt
    cnt+=1
    visited[v]=cnt*d
    answer+=visited[v]
    graph[v].sort()
    for i in graph[v]:
        if visited[i] == -1:
            dfs(i,d+1)
dfs(R,0)
print(answer)