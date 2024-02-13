from collections import deque
import sys
N, M, R = map(int,sys.stdin.readline().rstrip().split())
visited=[0]*(N+1)
graph=[[] for _ in range(N+1)]
for i in range(M):
    u,v = map(int,sys.stdin.readline().rstrip().split())
    graph[u].append(v)
    graph[v].append(u)
for j in range(1,N+1):
    graph[j].sort()
cnt=1
def bfs(v):
    global cnt
    queue=deque([v])
    visited[v]=cnt
    while queue:
        V=queue.popleft()
        for k in graph[V]:
            if visited[k] == 0:
                queue.append(k)
                cnt+=1
                visited[k] = cnt

bfs(R)
print(*visited[1:],sep='\n')
