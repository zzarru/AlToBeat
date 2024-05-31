n = int(input())
dp=[1,1] + [0]*n
for i in range(2,n+1):
    dp[i]=(dp[i-2]+dp[i-1]+1)%1000000007
print(dp[n])