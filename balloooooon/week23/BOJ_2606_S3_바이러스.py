p = int(input())

graph = [[] for _ in range(p+1)]
visited = [0 for _ in range(p+1)]
n = int(input())
for _ in range(n):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(cur):

    visited[cur] = 1
    for nxt in graph[cur]:
        if not visited[nxt]:
            dfs(nxt)
dfs(1)
answer = visited.count(1)-1
print(answer)