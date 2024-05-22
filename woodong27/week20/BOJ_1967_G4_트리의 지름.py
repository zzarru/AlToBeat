# BOJ 1967 G4 트리의 지름

import sys

"""
어제 푼 문제랑 똑같게 풀었다.
임의의 한 점에서 탐색했을 때 가장 거리가 먼 곳이 트리의 정점 중 하나이고
해당 정점에서 다시 탐색했을 때 가장 긴 거리가 트리의 지름이다.
"""


def dfs(current):
    global visited

    for next_, weight_ in tree[current]:
        if visited[next_] == -1:
            visited[next_] = visited[current] + weight_
            dfs(next_)


if __name__ == '__main__':
    sys.setrecursionlimit(10_000 ** 2)
    enter = sys.stdin.readline

    n = int(enter())
    tree = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        a, b, c = map(int, enter().split())
        tree[a].append([b, c])
        tree[b].append([a, c])

    visited = [-1] * (n + 1)
    visited[1] = 0
    dfs(1)

    start = visited.index(max(visited))
    visited = [-1] * (n + 1)
    visited[start] = 0
    dfs(start)

    answer = max(visited)
    sys.stdout.write(f'{answer}\n')

