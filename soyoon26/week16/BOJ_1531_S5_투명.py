import sys
N,M=map(int,sys.stdin.readline().split())
board = [[0]*101 for _ in range (101)]
cnt=0
for n in range(N):
    a,b,c,d = map(int,sys.stdin.readline().split())
    for i in range(b,d+1):
        for j in range(a,c+1):
            board[i][j]+=1

for i in range(101):
    for j in range(101):
        if board[i][j] > M:
            cnt+=1
print(cnt)