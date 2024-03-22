import sys
sys.setrecursionlimit(10**9)

N,M,R=map(int,sys.stdin.readline().split())
graph=list([] for _ in range(N+1))
visited=[-1]*(N+1)
for i in range(M):
    u,v=map(int,sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)
cnt,answer = 0, 0
def dfs(v,dep):
    global cnt, answer
    cnt+=1
    visited[v] = cnt*dep
    answer += visited[v]
    graph[v].sort(reverse=True)
    for i in graph[v]:
        if visited[i] == -1:
            dfs(i,dep+1)
dfs(R,0)
print(answer)