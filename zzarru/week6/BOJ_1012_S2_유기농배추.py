import sys
sys.setrecursionlimit(10000)

# dfs를 통해서 배추 상하좌우 탐색한다.
def dfs(x, y, m, n, field):
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if (0 <= nx < m) and (0 <= ny < n):
            if field[ny][nx] == 1:
                field[ny][nx] = 0
                dfs(nx, ny, m, n, field)

T = int(sys.stdin.readline())
for _ in range(T):
    m, n, cabbages = map(int, sys.stdin.readline().split())
    # 밭의 크기만큼 이중 배열 만들기
    field = [[0 for row in range(m)] for col in range(n)]

    for __ in range(cabbages):
        x, y = map(int, sys.stdin.readline().split())
        # 배추가 심겨진 곳 표시하기
        field[y][x] = 1

    bug = 0
    for xi in range(m):
        for yi in range(n):
            if field[yi][xi] == 1:
                dfs(xi, yi, m, n, field)
                bug += 1
    print(bug)