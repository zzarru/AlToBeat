import sys
from collections import deque
N,M,R= map(int,sys.stdin.readline().rstrip().split())
graph = [[] for _ in range(N+1)]
visited=[0]*(N+1)
cnt=1
for i in range(M):
    u, v= map(int,sys.stdin.readline().rstrip().split())
    graph[u].append(v)
    graph[v].append(u)
for j in range(N+1):
    graph[j].sort(reverse=True)

def bfs(r) :
     global cnt
     queue = deque([r])
     visited[r]=cnt
     while queue:
         V=queue.popleft()
         for k in graph[V]:
             if visited[k] == 0:
                 cnt+=1
                 visited[k] = cnt
                 queue.append(k)

bfs(R)
print(*visited[1:],sep="\n")
#answer만들어서 cnt따로 정렬시키면 시간초과