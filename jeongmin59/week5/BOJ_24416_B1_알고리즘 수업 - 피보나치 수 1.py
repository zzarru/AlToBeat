# 24416_알고리즘 수업 - 피보나치 수 1
'''
- 피보나치 -> 재귀 대신 DP로 풀어보기
'''


def fib(N):
    f = [0] * (N+1)
    f[1] = f[2] = 1
    for i in range(3, N+1):
        f[i] = f[i-1] + f[i-2]

    return f[N]


def fibonacci(N):
    return N-2


N = int(input())

print(fib(N), fibonacci(N))
