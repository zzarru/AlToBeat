from collections import deque
import sys
N,M,R= map(int,sys.stdin.readline().split())
graph=[[]for _ in range(N+1)]
visited=[-1]*(N+1)
ans=[0]*(N+1)
answer=[]
for i in range(M):
    u,v=map(int,sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(N+1):
    graph[i].sort()

def bfs(r):
    cnt=1
    queue = deque([r])
    visited[r]=0
    ans[r]=cnt
    while queue:
        V=queue.popleft()
        for j in graph[V]:
            if visited[j] == -1:
                ans.append(j)
                queue.append(j)
                visited[j]=visited[V]+1
                cnt+=1
                ans[j]=cnt
                answer.append(visited[j]*ans[j])
bfs(R)
print(sum(answer))

# 10 1 1
# 1 6