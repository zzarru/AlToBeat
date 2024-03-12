# BOJ 11729 G5 하노이 탑 이동 순서

"""
하노이의 탑
1단계 : 가장 마지막 원판만 남기고, 나머지 원판은 두번째 막대로 옮긴다.
2단계 : 첫번째 막대에 남은 마지막 원판을 세번째 막대로 옮긴다.
3단계 : 남은 n-1개의 원판을 다시 세번째 막대로 옮기기 위해 1~2를 반복한다.

answer를 1씩 더하면서 했는데
하노이의 탑의 정답은 원판의 갯수^2 - 1이라서
answer = N ** 2 - 1로 표현할 수 있다.
"""


N = int(input())


def hanoi_tower(n, start, end):
    global answer, sequence_list
    answer += 1
    if n == 1:
        sequence_list.append((start, end))
        return

    hanoi_tower(n - 1, start, 6 - start - end)  # 1단계
    sequence_list.append((start, end))  # 2단계
    hanoi_tower(n - 1, 6 - start - end, end)  # 3단계(재귀 반복)


answer = 0
sequence_list = []
hanoi_tower(N, 1, 3)

print(answer)
for row in sequence_list:
    print(*row)
