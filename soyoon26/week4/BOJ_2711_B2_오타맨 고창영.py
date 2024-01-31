N=int(input())
for i in range(N):
    n,w=input().split()
    print(w[:int(n)-1]+w[int(n):])