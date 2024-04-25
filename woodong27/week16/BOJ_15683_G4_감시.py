# BOJ 15683 G4 감시
from copy import deepcopy

"""
브루트포스로 cctv가 감시할 수 있는 모든 경우를 확인하면 된다.
나는 dfs를 사용했다. 
cctv 감시 -> dfs로 체크를 진행할 때 마다 현재 board를 copy해서
cctv 감시구역을 표시하기 전 사무실 상태를 가지고 있어야 한다.
"""

n, m = map(int, input().split())
office = [list(map(int, input().split()))for _ in range(n)]

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]
cctv_type = {
    1: [[0], [1], [2], [3]],
    2: [[0, 2], [1, 3]],
    3: [[0, 1], [1, 2], [2, 3], [3, 0]],
    4: [[0, 1, 2], [0, 1, 3], [1, 2, 3], [2, 3, 0]],
    5: [[0, 1, 2, 3]]
}


def dfs(count, board):
    global answer
    if count == len(cctv):
        temp = 0
        for row in board:
            temp += row.count(0)
        answer = min(answer, temp)
        return

    copied_office = deepcopy(board)
    si, sj, number = cctv[count]
    for directions in cctv_type[number]:
        watch(copied_office, directions, si, sj)
        dfs(count + 1, copied_office)
        copied_office = deepcopy(board)


def watch(board, directions, si, sj):
    for direction in directions:
        k = 1
        while True:
            ni, nj = si + di[direction] * k, sj + dj[direction] * k
            if ni < 0 or ni >= n or nj < 0 or nj >= m:
                break
            if board[ni][nj] == 6:
                break
            if not board[ni][nj]:
                board[ni][nj] = '#'
            k += 1
            

cctv = []
for i in range(n):
    for j in range(m):
        if office[i][j] and office[i][j] != 6:
            cctv.append((i, j, office[i][j]))

answer = m * n  # 최악의 경우 모든 칸이 사각지대
dfs(0, office)
print(answer)
