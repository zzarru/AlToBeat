n, m = map(int, input().split())

# 최대 공약수 구하기
a = max(n, m)
b = min(n, m)

while b != 0:
    a, b = b, a%b

print(a)

# 최소 공배수 구하기
print(n*m//a)