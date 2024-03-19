# BOJ 1743 S1 음식물 피하기

"""
기본적인 dfs 문제
음식물 쓰레기(#)을 만나면 해당 지점부터 탐색을 시작하면 된다.
탐색이 끝난 후에는 최종적으로 이동한 횟수를 반환해서
정답과 비교한다.
"""

import sys

sys.setrecursionlimit(100 ** 2)

n, m, k = map(int, input().split())

aisle = [['.' for _ in range(m)]for _ in range(n)]
for _ in range(k):
    i, j = map(int, input().split())
    aisle[i-1][j-1] = '#'


def dfs(si, sj):
    global count
    for di, dj in ((0, -1), (0, 1), (1, 0), (-1, 0)):
        ni, nj = si + di, sj + dj
        if 0 <= ni < n and 0 <= nj < m:
            if aisle[ni][nj] == '#' and not visited[ni][nj]:
                visited[ni][nj] = 1
                count += 1
                dfs(ni, nj)


answer = 0
visited = [[0 for _ in range(m)]for _ in range(n)]
for i in range(n):
    for j in range(m):
        if aisle[i][j] == '#' and not visited[i][j]:
            count = 0
            dfs(i, j)
            answer = max(answer, count)

print(answer)
