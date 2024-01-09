# 프로그래머스 [PCCE 기출문제]9번 : 이웃한 칸

def solution(board, h, w):
    answer = 0
    
    # 현재 입력된 보드의 길이 
    length = len(board[0])

    # 상하좌우 칸 중 [h][w]칸과 동일한 색의 칸 확인 후 count증가
    for di, dj in ((0, 1), (0, -1), (-1, 0), (1, 0)):
        ni, nj = h + di, w + dj
        if 0 <= ni < length and 0 <= nj < length:
            if board[ni][nj] == board[h][w]:
                answer += 1

    return answer
