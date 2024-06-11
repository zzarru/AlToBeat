# BOJ 5972 G5 택배 배송

"""
데이크스트라 기본 문제
"""

import sys
from heapq import heappush, heappop


def dijkstra():
    q = []
    heappush(q, (0, 1))
    while q:
        weight, current = heappop(q)
        if distance[current] >= weight:
            for next_, weight_ in loads[current]:
                if weight + weight_ < distance[next_]:
                    distance[next_] = weight + weight_
                    heappush(q, [weight + weight_, next_])


if __name__ == '__main__':
    enter = sys.stdin.readline
    n, m = map(int, enter().split())
    loads = [[] for _ in range(n + 1)]

    for _ in range(m):
        a, b, c = map(int, enter().split())
        loads[a].append([b, c])
        loads[b].append([a, c])

    distance = [float('inf')] * (n + 1)
    distance[1] = 0
    dijkstra()

    sys.stdout.write(f'{distance[n]}\n')
