import sys
n,m=map(int,sys.stdin.readline().split())
board = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

xy=[]
for i in range(n):
    for j in range(m):
        if board[i][j] == 1:
            xy.append([i,j])

ans = abs(xy[1][0]-xy[0][0]) + abs(xy[1][1]-xy[0][1])
print(ans)