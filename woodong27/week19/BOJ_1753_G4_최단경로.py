# BOJ 1753 G4 최단경로

from heapq import heappush, heappop
import sys


def dijkstra(start):
    q = []
    heappush(q, (0, start))
    distance = [float('inf')] * (v + 1)
    distance[start] = 0

    while q:
        weight, current = heappop(q)
        if distance[current] >= weight:
            for next_, weight_ in graph[current]:
                if weight + weight_ < distance[next_]:
                    distance[next_] = weight + weight_
                    heappush(q, (weight + weight_, next_))

    return distance[1:]


if __name__ == '__main__':
    enter = sys.stdin.readline
    v, e = map(int, enter().split())
    graph = [[] for _ in range(v + 1)]
    k = int(enter())
    for _ in range(e):
        a, b, c = map(int, enter().split())
        graph[a].append([b, c])

    result = dijkstra(k)
    print(*[str(value).upper() if value == float('inf') else value for value in result], sep='\n')
