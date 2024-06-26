tc = int(input())
for _ in range(tc):
    N = int(input())
    dp = [0 for _ in range(36)]
    dp[1] = dp[2] = dp[3] = 1
    n = 0
    while n<N:
        for i in [1,2,3]:
            if n+i<=N:
                dp[n + i] += dp[n]
        n+=1
    print(dp[N])