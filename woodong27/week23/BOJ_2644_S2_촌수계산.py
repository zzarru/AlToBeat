# BOJ 2644 S2 촌수계산

"""
기본적인 bfs 문제
"""

import sys
from collections import deque


def bfs(s, e):
    q = deque([(s, 0)])
    visited = [0] * (n + 1)
    visited[s] = 1
    while q:
        current, count = q.popleft()
        if current == e:
            return count
        for node in relations[current]:
            if not visited[node]:
                visited[node] = 1
                q.append((node, count + 1))

    return -1


if __name__ == '__main__':
    enter = sys.stdin.readline
    n = int(enter())
    start, end = map(int, enter().split())
    m = int(enter())
    relations = [[] for _ in range(n + 1)]
    for _ in range(m):
        x, y = map(int, enter().split())
        relations[x].append(y)
        relations[y].append(x)

    answer = bfs(start, end)
    sys.stdout.write(f'{answer}\n')
