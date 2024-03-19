# BOJ 7562 S1 나이트의 이동

"""
체스 기물 중 나이트가 이동할 수 있는 8가지 경우에 대해서
각각 이동을 시키면서 너비우선탐색을 진행한다.
만약 큐에서 뽑아낸 현재 좌표가 목적지와 같다면,
현재 좌표까지 이동하는데 걸린 거리를 정답으로 반환한다.
"""

from collections import deque

t = int(input())


def moving(i, j):
    q = deque([(i, j)])
    while q:
        ci, cj = q.popleft()
        if ci == gi and cj == gj:
            return visited[ci][cj] - 1
        # 나이트가 움직일 수 있는 8가지 경우에 대해서 이동
        for di, dj in ((-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, -2), (2, -1), (2, 1), (1, 2)):
            ni, nj = ci + di, cj + dj
            if 0 <= ni < l and 0 <= nj < l:
                if not visited[ni][nj]:
                    q.append((ni, nj))
                    visited[ni][nj] = visited[ci][cj] + 1


for _ in range(t):
    # 체스판 한 변의 길이
    l = int(input())
    # 현재 나이트의 위치
    si, sj = map(int, input().split())
    # 목적지
    gi, gj = map(int, input().split())

    board = [[0 for _ in range(l)]for _ in range(l)]
    visited = [[0 for _ in range(l)]for _ in range(l)]
    visited[si][sj] = 1

    answer = moving(si, sj)
    print(answer)
