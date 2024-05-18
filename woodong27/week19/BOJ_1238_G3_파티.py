# BOJ 1238 G3 파티

"""
x(도착지)에서 각 지점으로 돌아가는 시간을 하고
각 출발지에서 도착지까지의 시간을 구해서
왕복에 걸리는 시간이 가장 큰 값을 출력한다.

파이썬의 kwargs를 사용해서 도착지에서 돌아오는 탐색과
출발지에서 도착지로 이동하는 탐색을 구분했다.
"""

from heapq import heappush, heappop


def dijkstra(start, **kwargs):
    end = kwargs.get('end', False)

    q = []
    distance = [float('inf')] * (n + 1)
    distance[start] = 0
    heappush(q, [0, start])
    while q:
        weight, current = heappop(q)
        if end and current == end:
            return distance[end]

        if distance[current] >= weight:
            for next_, weight_ in villages[current]:
                if weight + weight_ < distance[next_]:
                    distance[next_] = weight + weight_
                    heappush(q, [weight + weight_, next_])

    return distance


if __name__ == '__main__':
    n, m, x = map(int, input().split())
    villages = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b, c = map(int, input().split())
        villages[a].append([b, c])

    from_x = dijkstra(x)
    answer = 0
    for i in range(1, n + 1):
        result = dijkstra(i, end=x)
        answer = max(answer, from_x[i] + result)

    print(answer)
