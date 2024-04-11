import sys
n, k = map(int,sys.stdin.readline().split())
coins = list(int(sys.stdin.readline().rstrip()) for _ in range(n))
cnt=0
for i in range(n-1,-1,-1):
    cnt+=k//coins[i]
    k=k%coins[i]
print(cnt)