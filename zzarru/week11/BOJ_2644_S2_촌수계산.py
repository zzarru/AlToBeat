N = int(input())
a, b = map(int, input().split())
M = int(input())
graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)
answer = []

for _ in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

# dfs
def dfs(v, num):
  num += 1
  visited[v] = True

  if v == b:
    answer.append(num)

  for i in graph[v]:
    if not visited[i]:
      dfs(i, num)

dfs(a, 0)
if len(answer) == 0:
  print(-1)
else:
  print(answer[0]-1)