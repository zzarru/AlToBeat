import sys
from collections import deque
N, M, R = map(int,sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]
visited=[-1]*(N+1)
for i in range(M):
    u, v = map(int,sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)
for j in range(1,N+1):
    graph[j].sort()

def bfs(r):
    queue = deque([r])
    visited[R]=0
    while queue:
        V = queue.popleft()
        for k in graph[V]:
            if visited[k] == -1 :
                visited[k] = visited[V]+1
                queue.append(k)
bfs(R)
print(*visited[1:],sep="\n")