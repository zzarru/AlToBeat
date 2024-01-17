N=int(input())
for i in range(N):
    if N%2 == 0:
        print('*'+' *'*(N//2-1))
        print(' *'*(N//2))
    else:
        print('*'+' *'*(N//2))
        print(' '+'* '*(N//2))