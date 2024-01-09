# 프로그래머스 2024 KAKAO WINTER INTERSHIP lv1 가장 많이 받은 선물

def solution(friends, gifts):
    answer = 0
    
    # 총 진구들의 수
    friends_number = len(friends)
    
    # 선물을 주고받은 관계를 나타낼 2차원 배열
    board = [[0 for _ in range(friends_number)]for _ in range(friends_number)]
    
    # 서로 주고 받은 선물 갯수를 카운트해서 board에 저장
    for gift in gifts:
        give, get = gift.split(' ')
        give_index = friends.index(give)
        get_index = friends.index(get)
        board[give_index][get_index] += 1
    
    # board의 전치행렬
    transposed_board = list(map(list, zip(*board)))
    
    # 각 친구의 선물지수 계산
    gift_grade = [0] * friends_number
    for i in range(friends_number):
        total_get = sum(transposed_board[i])
        total_give = sum(board[i])
        gift_grade[i] = total_give - total_get
    
    # 받아야 할 선물 계산
    result = [0] * friends_number
    for i in range(friends_number):
        for j in range(friends_number):
            if i != j:
                if board[i][j] > board[j][i]:
                    result[i] += 1
                elif board[i][j] == board[j][i]:
                    if gift_grade[i] > gift_grade[j]:
                        result[i] += 1
    
    answer = max(result)
    return answer
