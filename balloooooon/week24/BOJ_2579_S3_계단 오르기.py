'''
dp를 2차원으로 선언하였는데 0행의 dp는 방금 1칸 올라왔다고 가정 그럼 다음은 무조건 2칸 올라가야함
1행의 dp는 방금 2칸 올라왔다고 가정 그럼 다음은 1칸 또는 2칸 올라갈 수 있음
매번 계단의 누적이 최대가 되어야하므로 max로 dp를 갱신
처음 시작이 중요한데 첫스타트를 첫계단에서 할 수도 있지만
2번째 계단에서 할 수도 있음을 염두해야함 => dp[0][1] = steps[1]
'''

N= int(input())
if N > 1:
    steps = [0 for _ in range(N)]
    for i in range(N):
        cost = int(input())
        steps[i] = cost

    dp = [[0 for i in range(N)], [0 for i in range(N)]]
    dp[1][0] = steps[0]
    dp[0][0] = steps[0]
    dp[0][1] = steps[1]
    for n in range(N):

        if n+1 < N :
            dp[1][n+1] = max(steps[n+1] + dp[0][n], dp[1][n+1])
        if n+2 < N :
            dp[1][n+2] = max(steps[n+2] + dp[1][n] , dp[1][n+2])
            dp[0][n+2] = max(steps[n+2] + dp[1][n] , dp[0][n+2])
    print(max(dp[0][N-1],dp[1][N-1]))
else:
    print(int(input()))