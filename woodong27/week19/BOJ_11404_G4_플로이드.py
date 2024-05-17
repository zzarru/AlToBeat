# BOJ 11404 G4 플로이드

"""
기본적인 플로이드 워셜 알고리즘 문제
"""

import sys


if __name__ == '__main__':
    enter = sys.stdin.readline
    n = int(enter())
    m = int(enter())

    distance = [[float('inf') for _ in range(n)]for _ in range(n)]
    for i in range(n):
        distance[i][i] = 0

    for _ in range(m):
        a, b, c = map(int, enter().strip().split())
        distance[a-1][b-1] = min(distance[a-1][b-1], c)

    for k in range(n):
        for i in range(n):
            for j in range(n):
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])

    for row in distance:
        if float('inf') in row:
            row = [value if value != float('inf') else 0 for value in row]
        print(*row)
