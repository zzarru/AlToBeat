# Week17(최단 경로, Shortest Path)

BFS, 플로이드 워셜, 데이크스트라(다익스트라), 벨만 포드 알고리즘을 사용할 수 있다.

### 데이크스트라(Dijkstra)

한 노드에서 다른 노드까지의 최단거리를 구하는 알고리즘이다.

heap과 greedy 알고리즘을 사용하여 최단거리를 구하며, 모든 간선의 가중치가 양수일때만 사용할 수 있다.

```python
import heapq

n, m = map(int, input().split())  # 노드와 간선의 갯수
graph = [[] for _ in range(n + 1)]
distance = [float('inf')] * (n + 1)  # 각 노드간의 거리를 무한(최대)로 임의로 지정

for _ in range(m):
    u, v, w = map(int, input().split())  # 출발, 도착, 가중치
    graph[u].append((v, w))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))  # 우선순위, 노드의 값 형태로 heap에 넣는다
    distance[start] = 0  # 자기 자신과의 거리는 0

    while q:
        weight, current = heapq.heappop(q)  # 우선순위가 가장 낮은(=가장 가까운 노드)가 pop 된다.
        
        if distance[current] >= weight:  # 방문했던 노드가 아니거나, 현재의 가중치가 더 작을 경우에만 탐색한다.
            for node, weight_ in graph[current]:
                if weight + weight_ < distance[node]:  # 기존의 값(inf 또는 기존에 방문했던 거리)보다 작은 경우에만 탐색
                    distance[node] = weight + weight_
                    heapq.heappush(q, (weight + weight_, node))

dijkstra(s)          
```

### 벨만 포드(Bellman Ford)

데이크스트라와 동일하게 한 노드에서 다른 노드까지의 최단거리를 구하지만, 가중치가 음수인 간선이 존재할 때도 사용할 수 있다.

n-1번 루프를 돌며 거리배열을 업데이트하고, n번째 루프에도 업데이트가 일어나면 음수싸이클이 존재하게 되는 것을 이용한다.

음수 가중치 간선을 처리할 수 있지만, 데이크스트라에 비해서 시간 복잡도가 느리다.

```python
def bellman_ford(graph, start):
    distance = [float('inf')] * (n + 1)
    distance[start] = 0  # 자기 자신과의 거리는 0

    for _ in range(n):  # 노드의 수 - 1 번 만큼 반복
        for i in range(1, n + 1):
            for node, weight in graph[i]:
                if distance[i] + weight < distance[node]:
                    distance[node] = distance[i] + weight

    for i in range(1, n + 1):  # 음수 가중치 경로가 있는지 확인
        for node, weight in graph[i]:
            if distance[i] + weight < distance[node]:
                raise ValueError("음수 가중치 사이클")
    
graph = [
    [],
    [[2, -1], [3, 4]],  # [도착지, 가중치] 쌍
    [[1, 1], [3, 2], [4, 5]],
    [[1, 4], [2, 2], [4, 1]],
    [[2, 5], [3, -1]]
]

bellman_ford(graph, 1)
print(distance)  # [inf, 0, -1, 1, 2]
```

### 플로이드 워셜(Floyd Warshall)

임의의 두 노드간의 최단거리를 한 번에 구하는 알고리즘이다.

2차원 배열로 모든 경우의 수를 다 따져서 모든 노드간의 최단거리를 구한다.

DP(Dynamic Programming)을 사용한 알고리즘으로, 시작노드를 따로 지정할 필요가 없다.

모든 노드에 대해서 각 노드간의 최단 거리를 찾기 때문에 데이크스트라와 벨만 포드에 비해서 더 많은 계산을 수행한다.

```python
def floyd_warshal(graph):
    distance = [[float('inf') for _ in range(n + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for node, weight in graph[i]:
            distance[i][node] = weight
            distance[node][i] = weight  # 양방향 간선일 경우

    for i in range(1, n + 1):
        distance[i][i] = 0  # 자기 자신과의 거리는 0

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            for k in range(1, n + 1):  # 거쳐가는 노드에 따라서 최소값으로 거리 업데이트
                distance[j][k] = min(distance[j][k], distance[j][i] + distance[i][k])
```