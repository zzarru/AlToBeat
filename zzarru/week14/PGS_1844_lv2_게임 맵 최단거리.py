from collections import deque

def solution(maps):
    answer = 0
    dx = [-1, 1, 0, 0]  # 동서남북 +1칸
    dy = [0, 0, -1, 1]

    queue = deque()
    queue.append((0, 0))  # start

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            N, M = len(maps), len(maps[0])
            if 0 <= nx < N and 0 <= ny < M and maps[nx][ny] == 1:
                maps[nx][ny] = maps[x][y] + 1  # 지나온 길의 최단 거리를 더한다.
                queue.append((nx, ny))

    answer = maps[N - 1][M - 1]

    if answer == 1:
        answer = -1
    return answer