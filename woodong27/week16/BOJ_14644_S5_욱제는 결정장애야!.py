# BOJ 14644 S5 욱제는 결정장애야!

"""
딴거 풀다가 너무 안돼서 포기했다.
BOJ 20055 컨베이어 벨트 위의 로봇 나중에 다시 풀어야함
"""

n = int(input())
menus = list(map(int, input().split()))

board = [0] * (n + 1)

answer, count = 0, 0
for menu in menus:
    if not board[menu]:
        count += 1
        board[menu] = 1
    else:
        count -= 1

    answer = max(answer, count)

print(answer)
