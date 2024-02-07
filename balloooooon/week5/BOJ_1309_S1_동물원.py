# dp는 전의 결과를 이용해서 다음 결과를 만들어 내는 것임을 항상 주시해야한다
# 이문제의 특수한 조건에 의해 다음과 같은 규칙이 만들어진다
# n번째는 
# 위쪽에 한칸이 붙은경우, 아래쪽에 한칸이 붙은 경우, 각각 결과가 일대일대응되는 n-1번째의 경우의 수
# 위든 아래든 한칸이 붙었으나 맨위와 맨아래는 비우는 경우 -> n-2번째의 경우의 수와 같다
import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 8)

dp = {}
def f(n):
    if n in dp:
        return dp[n]
    if n==0:
        dp[0]=0
        return 1
    if n == 1:
        dp[1]=3
        return 3

    if n >= 2:
        dp[n]=2*f(n - 1)%9901 + f(n - 2)%9901
        return dp[n]%9901

print((f(int(input().rstrip()))))