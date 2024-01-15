N = int(input())
for i in range(1,2*N+1):
    if i <= N:
        print(i*'*'+(N-i)*'  '+i*'*')
    else:
        print((2*N-i)*'*'+(i-N)*'  '+(2*N-i)*'*')