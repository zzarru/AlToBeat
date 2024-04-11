# BOJ 11497 S1 통나무 건너뛰기

"""
입력받은 리스트를 정렬한 뒤
인덱스가 2씩 차이나도록 오름차순 ~ 내림자순으로 정렬하면
가장 난이도가 낮은 경우의 모습이 된다.
"""

T = int(input())

for _ in range(T):
    N = int(input())
    logs = list(map(int, input().split()))

    logs.sort()
    result = [0] * N
    left, right = 0, N-1
    for i in range(N):
        if i % 2:
            result[right] = logs[i]
            right -= 1
        else:
            result[left] = logs[i]
            left += 1

    answer = max(abs(result[0] - result[-1]), 0)
    for i in range(N-1):
        answer = max(answer, abs(result[i] - result[i+1]))

    print(answer)
