# BOJ 9251 G5 LCS

"""
첫번째 단어의 문자와
두번째의 문자가 같은 경우, 다른 경우 두가지로 구분한다.
같다면 이전까지의 LCS길이에 +1을 해주고
다르면 이전의 LCS길이 중 최대값을 가져온다.
"""

import sys


if __name__ == '__main__':
    enter = sys.stdin.readline
    first = enter().strip()
    second = enter().strip()

    dp = [[0 for _ in range(len(second) + 1)]for _ in range(len(first) + 1)]

    for i in range(1, len(first) + 1):
        for j in range(1, len(second) + 1):
            if first[i-1] == second[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    answer = max([item for row in dp for item in row])
    sys.stdout.write(f'{answer}\n')
