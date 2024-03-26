import sys
N,M=map(int,sys.stdin.readline().split())
board=[list(map(int,list(sys.stdin.readline().rstrip()))) for _ in range(N)]
ans=[1]
for _ in range(N):
    for i in range(M):
        for j in range(i+1,M):
            if board[_][i] == board[_][j]:
                try:
                    if board[_][i] == board[_+(j-i)][i] and board[_][i] == board[_+(j-i)][j]:
                        ans.append((j-i+1)**2)
                except:
                    continue
print(max(ans))