# BOJ 2559 S3 수열

"""
투 포인터 연습용 문제
슬라이딩 윈도우랑 비슷한 느낌으로 풀면 될 것 같다.
"""

n, k = map(int, input().split())
numbers = list(map(int, input().split()))

end, temp = 0, 0
answer = -100 * k  # 최악의 경우
for start in range(n - k + 1):
    while end <= n:
        if end - start == k:
            answer = max(answer, temp)
            temp -= numbers[start]
            break
        temp += numbers[end]
        end += 1

print(answer)
