# BOJ 14499 G4 주사위 굴리기

"""
각 방위로 주사위를 굴렸을 때의 결과를 확인하고
주사위를 굴리는 메서드를 구현하였다.
이후에는 이동한 칸이 0이거나 0이 아닌 경우에 따라서
동작을 수행하고, 주사위의 윗면(0번 인덱스)를 출력하면 된다.
"""

n, m, si, sj, k = map(int, input().split())
board = [list(map(int, input().split()))for _ in range(n)]
orders = list(map(int, input().split()))

move = [(0, 1), (0, -1), (-1, 0), (1, 0)]  # 동, 서, 북, 남
dice = [0, 0, 0, 0, 0, 0]


def turn(direction):
    """
    각 방향으로 주사위를 굴렸을 때의 결과를 저장
    :param direction: 주사위를 굴리는 방향
    :return:
    """

    global dice
    a, b, c, d, e, f = dice
    if direction == 1:  # 동
        dice = [d, b, a, f, e, c]
    elif direction == 2:  # 서
        dice = [c, b, f, a, e, d]
    elif direction == 3:  # 북
        dice = [e, a, c, d, f, b]
    else:  # 남
        dice = [b, f, c, d, a, e]


for order in orders:
    ni, nj = si + move[order-1][0], sj + move[order-1][1]
    if 0 <= ni < n and 0 <= nj < m:
        si, sj = ni, nj
        turn(order)
        if board[si][sj]:  # 이동한 칸에 숫자가 있을 경우
            dice[-1] = board[si][sj]
            board[si][sj] = 0
        else:  # 이동한 칸이 0일 경우
            board[si][sj] = dice[-1]

        print(dice[0])
