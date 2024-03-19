# BOJ 11722 S2 가장 긴 감소하는 부분 수열

"""
가장 긴 증가하는 부분 수열(LIS) 알고리즘과 반대로 풀면 된다.
완전탐색, DP, 이진탐색으로 구현 가능하며
이번 문제에서는 DP를 사용했다.
"""

n = int(input())

numbers = list(map(int, input().split()))

dp = [1] * n

# 현재 숫자가 비교해야할 이전의 숫자들보다 더 작다면
# 그 숫자까지의 길이 + 1과 현재 자신의 길이를 비교해서 더 큰 값을 할당한다.
for i in range(1, n):
    for j in range(i):
        if numbers[i] < numbers[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))
