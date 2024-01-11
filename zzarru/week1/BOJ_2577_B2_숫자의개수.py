A = int(input())
B = int(input())
C = int(input())
X = str(A*B*C)

# 각 자릿 수의 숫자를 세기 위한 배열을 만든다.
counter = list(0 for _ in range(10))

for i in X:
    counter[int(i)] += 1

for ans in counter:
    print(ans)