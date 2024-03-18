# BOJ 11052 S1 카드 구매하기

"""
점화식 규칙
dp[1] = cards[1]
dp[2] = max(dp[1] + dp[1], cards[2])
dp[3] = max(dp[1] + cards[2], dp[2] + cards[1], cards[3])
dp[4] = max(dp[1] + cards[3], dp[2] + cards[2], dp[3] + cards[1], cards[4])
-> 이중반복문을 사용하면 된다.
"""

n = int(input())

cards = [0] + list(map(int, input().split()))

dp = [0] * (n + 1)

for i in range(1, n + 1):
    for j in range(1, i + 1):
        dp[i] = max(dp[i], dp[i-j] + cards[j])

print(dp[n])
