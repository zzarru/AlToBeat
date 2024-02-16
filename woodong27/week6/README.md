# week6(BFS, 너비우선탐색)

## BFS(Breadth-First Search)

그래프의 시작노드에서 인접한 노드부터 순서대로 탐색하는 알고리즘이다.

이동에 드는 비용이 모두 동일한 조건에서 최단거리를 구하는 문제를 효과적으로 해결할 수 있다.

E.g : 미로를 빠져나가는 최단거리 등

Queue(큐) 자료구조를 활용하여, 인접한 노드를 큐에 삽입하고 삽입된 순서대로 꺼내서 이동한다.

```python
# BFS 예시

# deque 라이브러리를 불러와서 사용한다.
from collections import deque

def bfs(graph, start_node, visited):
    q = deque([start_node])
    # 시작노드는 방문처리
    visited[start_node] = 1

    while q:
        # 선입선출 -> popleft 사용
        current = q.popleft()
        # 현재 노드에서 아직 방문하지 않았고, 이동할 수 있는 노드들을 순서대로 이동한다.
        for node in graph[current]:
            if not visited[node]:
                q.append(node)
                visited[node] = 1
```

### BFS 예시 - 그래프에서 이동 경로 찾기

|       | **1** | **2** | **3** | **4** | **5** |
| ----- | ----- | ----- | ----- | ----- | ----- |
| **1** | x     | x     | o     | x     | o     |
| **2** | x     | x     | x     | o     | x     |
| **3** | o     | x     | x     | o     | o     |
| **4** | x     | o     | o     | x     | x     |
| **5** | o     | x     | o     | x     | x     |

해당 그래프는 아래와 같은 양방향 간선으로 연걸되어 있다.

```markdown
1 - 3 / 1 - 5 / 2 - 4 / 3 - 4 / 3 - 5
```

해당 그래프에서 1번 노드에서부터 시작하는 bfs를 진행하면 아래와 같은 결과가 나온다.

```python
from collections import deque

# 노드의 갯수, 간선의 수
n, m = map(int, input().split())

graph = [[0 for _ in range(n + 1)]for _ in range(n + 1)]
for _ in range(m):
    start, end = map(int, input().split())
    graph[start][end] = 1
    graph[end][start] = 1

# 1번 노드부터 bfs를 시작한다.
q = deque([1])
visited = [0 for _ in range(n + 1)]
visited[1] = 1
while q:
    current_node = q.popleft()
    print(current_node)
    for next_node in range(1, n + 1):
        if graph[current_node][next_node] and not visited[next_node]:
            q.append(next_node)
            visited[next_node] = 1

# 입력
# 5 4
# 1 3
# 1 5
# 2 4
# 3 4
# 3 5

# 결과
# 1
# 3
# 5
# 4
# 2
```

해당 그래프에서 1번 노드에서 부터 이동을 시작하면

1 - 3 - 5 - 4 - 2 순서로 이동하는 것을 확인할 수 있다.
