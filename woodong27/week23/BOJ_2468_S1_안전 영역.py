# BOJ 2468 S1 안전 영역

"""
0 ~ 최대값 사이의 비가 내리는 모든 경우를 검사하면 된다.
"""

import sys
from collections import deque


def bfs(si, sj):
    q = deque([(si, sj)])
    while q:
        ci, cj = q.popleft()
        for di, dj in ((-1, 0), (0, -1), (1, 0), (0, 1)):
            ni, nj = ci + di, cj + dj
            if 0 <= ni < n and 0 <= nj < n and not visited[ni][nj]:
                visited[ni][nj] = 1
                q.append((ni, nj))


if __name__ == '__main__':
    enter = sys.stdin.readline
    n = int(enter())
    area = [list(map(int, enter().split())) for _ in range(n)]

    max_value = max([max(row) for row in area])
    rain = 0
    answer = 0
    while True:
        visited = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if area[i][j] <= rain:
                    visited[i][j] = 1

        count = 0
        for i in range(n):
            for j in range(n):
                if not visited[i][j]:
                    visited[i][j] = 1
                    count += 1
                    bfs(i, j)

        answer = max(answer, count)
        rain += 1
        if rain > max_value:
            break

    sys.stdout.write(f'{answer}\n')
