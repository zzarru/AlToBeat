N = int(input())
print(' '*(N-1)+'*')
for i in range(1,N):
    print(' '*(N-i-1)+'*'+' '*(2*i-1)+'*')
