# Week11(DFS, 깊이 우선 탐색)

BFS와 같은 그래프 탐색 알고리즘

스택을 사용하거나 재귀를 통해서 구현할 수 있다.

시작점에서 펴저나가듯이 탐색하는 bfs와 달리

한 방향을 정해서 끝까지 탐색한 후에 다시 돌아와서 탐색하는 방법

### 스택을 이용한 방법

```python
def dfs(start):
    stack = [start]
    while stack:
        current = stack.pop()
        for node in graph[current]:
            if not visited[node]:
                visited[node] = True
                stack.append(node)
```

### 재귀를 이용한 방법

```python
def dfs(start):
    for node in graph[start]:
        if not visited[node]:
            visited[node] = True
            dfs(node)
```
