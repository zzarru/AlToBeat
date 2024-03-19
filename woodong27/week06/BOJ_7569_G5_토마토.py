# BOJ 7569 G5 토마토

"""
3차원 행렬에 대해서 bfs를 실행하면 된다.
bfs후에 0으로 익지 않은 토마토가 있다면 -1을 반환한다.
이외에는 가장 익는데 오래걸린 토마토를 반환하면 된다.
"""

from collections import deque


def bfs(positions):
    q = deque(positions)
    while q:
        ck, ci, cj = q.popleft()
        for dk, di, dj in ((0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1), (-1, 0, 0), (1, 0, 0)):
            nk, ni, nj = ck + dk, ci + di, cj + dj
            if 0 <= nk < h and 0 <= ni < n and 0 <= nj < m:
                if not tomatoes[nk][ni][nj]:
                    tomatoes[nk][ni][nj] = tomatoes[ck][ci][cj] + 1
                    q.append((nk, ni, nj))


m, n, h = map(int, input().split())

tomatoes = []
start_points = []

for _ in range(h):
    floor = [list(map(int, input().split()))for _ in range(n)]
    tomatoes.append(floor)

visited = [[[0 for _ in range(m)]for _ in range(n)]for _ in range(h)]

for k in range(h):
    for i in range(n):
        for j in range(m):
            if tomatoes[k][i][j] == 1:
                start_points.append([k, i, j])

bfs(start_points)

zero_count = 0
max_count = 0
for floor in tomatoes:
    for col in floor:
        zero_count += col.count(0)
        max_count = max(max_count, max(col))

answer = max_count - 1
if zero_count > 0:
    answer = -1

print(answer)
