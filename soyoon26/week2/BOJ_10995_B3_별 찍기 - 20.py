N = int(input())
for i in range(1,N+1):
    if i%2:
        print('*'+' *'*(N-1))
    else:
        print(' *'+' *'*(N-1))