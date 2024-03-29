# BOJ 1107 G5 리모컨

"""
처음에는 재귀로 풀어야 하나 생각했지만..
파이썬에서 for-else 문을 그동안 전혀 안썼는데
꼭 써야 하는 문제는 아니지만 문맥상 쓰는게 더 맞는 것 같다고 생각되었다.

0 ~ 9번버튼이 모두 고장나면 100만부터 하나씩 내려와야 하기 때문에
i의 범위는 0 ~ 100만으로 설정해야 한다.
"""

N = int(input())
M = int(input())
broken = list(input().split()) if M else []
start = 100

answer = abs(N - start)  # 최악의 경우(모두 +나 -버튼으로만 이동)
for i in range(1000001):  # 0 ~ 9번 버튼이 모두 고장나면 최악의 경우 100만부터 내려와야 한다.\
    number = str(i)
    for n in number:
        if broken and n in broken:
            break
    else:
        # 현재 번호를 누른 횟수 : len(number)
        # 현재부터 목적지까지 +나 - 버튼을 누르는 횟수 : abs(i - N)
        answer = min(answer, len(number) + abs(i - N))

print(answer)
