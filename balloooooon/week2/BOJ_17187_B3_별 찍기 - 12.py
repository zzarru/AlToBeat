# 별찍기 그런데 마지막 줄이 한줄 개행되어서 코드가 예쁘지 않다.

N = int(input())

for i in range(1,N):
    print(' '*(N-1-i), '*' * i)
for i in range(N,0,-1):
    if i == 1:
        print(' ' * (N - i) + '*' * i, end='')
    else:
        print(' ' * (N - i) + '*' * i,)

