# BOJ 14940 S1 쉬운 최단거리

"""
bfs 탐색 후에 지도가 -1로 갈 수 없지만 visited가 0이 아닌 지점들은
모두 0으로 변경해줘야 한다.
"""

import sys
from collections import deque


def bfs(si, sj):
    q = deque([(si, sj)])
    while q:
        ci, cj = q.popleft()
        for di, dj in ((0, -1), (-1, 0), (0, 1), (1, 0)):
            ni, nj = ci + di, cj + dj
            if 0 <= ni < n and 0 <= nj < m and visited[ni][nj] == -1:
                if not map_[ni][nj]:
                    visited[ni][nj] = 0
                else:
                    visited[ni][nj] = visited[ci][cj] + 1
                    q.append((ni, nj))


if __name__ == '__main__':
    enter = sys.stdin.readline
    n, m = map(int, enter().split())
    map_ = [list(map(int, enter().split()))for _ in range(n)]

    visited = [[-1] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if map_[i][j] == 2:
                visited[i][j] = 0
                bfs(i, j)

    for i in range(n):
        for j in range(m):
            if map_[i][j] == 0 and visited[i][j]:
                visited[i][j] = 0

    for row in visited:
        print(*row)
