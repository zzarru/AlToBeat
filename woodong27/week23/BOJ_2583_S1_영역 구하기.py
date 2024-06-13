# BOJ 2583 S1 영역 구하기

"""
기본적인 bfs 문제
"""

import sys
from collections import deque


def paint(sj, si, ej, ei):
    for i in range(si, ei):
        for j in range(sj, ej):
            board[i][j] = 1


def bfs(si, sj):
    count = 1
    q = deque([(si, sj)])
    while q:
        ci, cj = q.popleft()
        for di, dj in ((-1, 0), (0, -1), (1, 0), (0, 1)):
            ni, nj = ci + di, cj + dj
            if 0 <= ni < n and 0 <= nj < m and not board[ni][nj] and not visited[ni][nj]:
                visited[ni][nj] = 1
                count += 1
                q.append((ni, nj))

    return count


if __name__ == '__main__':
    enter = sys.stdin.readline
    n, m, k = map(int, enter().split())

    board = [[0] * m for _ in range(n)]
    for _ in range(k):
        paint(*map(int, enter().split()))

    visited = [[0] * m for _ in range(n)]
    answer = []
    for i in range(n):
        for j in range(m):
            if not board[i][j] and not visited[i][j]:
                visited[i][j] = 1
                answer.append(bfs(i, j))

    answer.sort()
    sys.stdout.write(f'{len(answer)}\n')
    print(*answer)
