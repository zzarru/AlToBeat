# #1 일반 구현
N = int(input())

Fibonacci = [0, 1]
for n in range(2, N+1):
    F = Fibonacci[n-2] + Fibonacci[n-1]
    Fibonacci.append(F)

print(Fibonacci[-1])

#2 재귀 함수로 풀어보기
# def Fibonacci(n):
#     F0 = 0
#     F1 = 1
#     Fn = 0
#     for _ in range(n-1):
#         Fn = F0 + F1
#         F0, F1 = F1, Fn
#
#     return Fn
#
# N = int(input())
# print(Fibonacci(N))