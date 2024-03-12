#1 for문을 통해서 구하기
N = int(input())
ans = 1
for i in range(1, N+1):
    ans = ans*i

print(ans)

#2 재귀를 이용하여 구하기
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

print(factorial(int(input())))