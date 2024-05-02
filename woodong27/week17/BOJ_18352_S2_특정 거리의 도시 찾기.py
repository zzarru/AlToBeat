# BOJ 18352 S2 특정 거리의 도시 찾기

"""
bfs로 풀어도 되지만, 연습을 위해 데이크스트라 알고리즘 사용

input()으로 했을 때 시간초과가 나서 sys.stdin으로 변경하고
다시 시간초과가 떠서 pypy3로 변경해서 통과
"""

import heapq
import sys

n, m, k, x = map(int, sys.stdin.readline().strip().split())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, sys.stdin.readline().strip().split())
    graph[a].append([b, 1])

distance = [float('inf')] * (n + 1)
q = []
heapq.heappush(q, (0, x))
distance[x] = 0

while q:
    weight, current = heapq.heappop(q)

    if distance[current] >= weight:
        for node_, weight_ in graph[current]:
            if weight + weight_ < distance[node_]:
                distance[node_] = weight + weight_
                heapq.heappush(q, (weight + weight_, node_))

result = [index for index, value in enumerate(distance) if value == k]

if not result:
    print(-1)
else:
    result.sort()
    print(*result, sep='\n')
