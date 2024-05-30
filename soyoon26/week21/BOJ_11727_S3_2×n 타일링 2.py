n=int(input())
dp=[0,1,3] + [0]*n
for i in range(3,n+1):
    dp[i] = (dp[i-1]+dp[i-2]*2)%10007
print(dp[n])