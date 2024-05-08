# BOJ 17835 G2 면접보는 슴범이네

"""
u도시에서 v도시로 가는 단방향 단선이라고 했는데
왜 graph[v].append(u)인지.. 이해가 안된다.

일단 graph[u].append(v)로 했을 때는 계속 실패했다.
"""

from heapq import heappush, heappop
import sys


def dijkstra():
    q = []
    for office in offices:
        heappush(q, [0, office])
        distance[office] = 0

    while q:
        weight, current = heappop(q)
        if distance[current] >= weight:
            for next_, weight_ in graph[current]:
                if weight + weight_ < distance[next_]:
                    distance[next_] = weight + weight_
                    heappush(q, [weight + weight_, next_])


if __name__ == '__main__':
    enter = sys.stdin.readline

    n, m, k = map(int, enter().strip().split())
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v, c = map(int, enter().strip().split())
        graph[v].append([u, c])
    offices = list(map(int, enter().strip().split()))

    distance = [float('inf')] * (n + 1)
    dijkstra()

    furthest = max(distance[1:])
    print(distance.index(furthest))
    print(furthest)
