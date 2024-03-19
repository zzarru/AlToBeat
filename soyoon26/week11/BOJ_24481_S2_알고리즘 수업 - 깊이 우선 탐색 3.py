import sys
sys.setrecursionlimit(10**6)
N,M,R=map(int,sys.stdin.readline().split())
graph=list([] for _ in range(N+1))
answer=[-1]*(N+1)
for m in range(M):
    u, v= map(int,sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)
cnt=1
def dfs(v,answer,cnt):
    answer[v]=cnt
    graph[v].sort()
    for i in graph[v]:
        if answer[i] == -1:
            dfs(i,answer,cnt+1)
dfs(R,answer,0)
print(*answer[1:],sep='\n')
