# BOJ 2156 S1 포도주 시식

"""
포도주는 연속 세 잔 이상 마실 수 없다.
1. 전전 와인(n - 2)를 마신 경우 : dp[n-2] + 현재 와인
2. 전 와인(n - 1)을 마신 경우 : dp[n-3] + 이전 와인 + 현재 와인
3. 전 와인(n - 1)을 마시고, 이번 와인을 만마실 경우 dp[n-1]
-> 세가지를 비교한다.
만약 현재 와인을 마시는게 dp[n-1]보다 작은 경우에는 dp[n-1]을 현재값으로 가져가야 하기 때문에
dp[n-1]과도 비교해줘야 한다.
"""

n = int(input())

glasses = [0] * 10001
for i in range(1, n + 1):
    glasses[i] = int(input())

dp = [0] * 10001

dp[1] = glasses[1]
dp[2] = glasses[1] + glasses[2]

for i in range(3, n + 1):
    dp[i] = max((dp[i-2] + glasses[i]), (dp[i-3] + glasses[i-1] + glasses[i]), dp[i-1])

print(dp[n])
