N=int(input())

dp = [1 for i in range(N+1)]
square_numbers = []

for num in range(1,N+1):
    if int(num**0.5) == num**0.5:
        square_numbers.append(num)
    else:
        temp_values = []
        for square_number in square_numbers:
            temp_values.append(dp[num-square_number] + 1) # temp_values.append(dp[num-square_number] + dp[square_number))와 같은 의미
        dp[num] = min(temp_values)
print(dp[N])

# 이 문제는 최소항의 갯수는 최소에 기인한다는 원리를 다시 한번 각인하는 문제였고, dp를 이용해 이전의 값을 활용해 다음의 값을
# 추론해 나가는 전형적인 포맷이었다.
# 1은 1이 1개, 2는 1이 2개, 3은 1이 3개, 그리고 4부터는 제곱수이므로 다시 1개
# 그렇다면 5는? 당연히 그전의 가장큰  제곱수인 4를 가져와서 나머지를 더하는 것이 합당하다
# dp[5] = dp[4] + dp[5-4] = dp[4] + dp[1]
# 그러면 그전까지 가장 컸던 제곱수만 가져오면되겠네?
# 문제 넘 쉽네 ㅋ 하다가 dp[18]에서 막혔다
# dp[18]의 경우 dp[16] + dp[2]가 가능은 하지만 최솟값은 아니다
# dp[9] + dp[18-9]가 있기때문
# 그렇다면 이러한 경우의 수들을 모두 다뤄서 '최솟값'을 찾아놓으면 되지않을까?
# 최솟값 후보들을 담을 temp_values라는 리스트를 만들어서 최솟값을 내주었다.
# 최소에서 최소로!
