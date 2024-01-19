N = int(input())
for i in range(1,2*N+1):
    if i <= N:
        print('*'*i)
    else:
        print('*'*(2*N-i))