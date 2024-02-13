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