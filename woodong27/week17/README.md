# Week17(최단 경로, Shortest Path)

BFS, 플로이드 워셜, 데이크스트라(다익스트라) 등의 알고리즘을 사용할 수 있다.

## 데이크스트라(Dijkstra)

각 노드들 간의 관계와 관계별 가중치(거리)가 주어졌을 때, 가장 짧은 거리를 탐색하는 알고리즘

heap을 사용해서 현재 노드에서 가장 짧은 노드를 사용하면 시간복잡도를 낮출 수 있다.

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