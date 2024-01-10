# 해당 문제는 좌표가 주어지면 델타탐색을 통해서 상하좌우를 조사할 수 있는지를 묻는 문제였다.

def solution(board, h, w):
    answer = 0
    max_length = len(board)
    di = [-1,1,0,0] # 행
    dj = [0,0,-1,1] # 열
    i = h
    j = w
    for k in range(4):
        ni = i + di[k] # ni와 nj를 정의해주고
        nj = j + dj[k]
        if 0 <= ni < max_length and 0 <= nj < max_length: # 미리 배열을 벗어날 부분을 걸러준다.
            if board[h][w] == board[ni][nj]:
                answer += 1
    return answer
