# 9655_돌 게임
'''
- 돌을 1개 또는 3개 가져갈 수 있을 때, 마지막 돌을 가져가는 사람이 게임을 이김
- 이기는 사람 출력, 게임은 상근이가 먼저 진행 하며 상근이가 이기면 SK, 창영이가 이기면 CY 출력
'''


def winner(N):
    if N % 2 == 0:
        return "CY"

    else:
        return "SK"


N = int(input())

print(winner(N))