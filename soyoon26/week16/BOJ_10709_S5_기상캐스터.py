import sys

h,w = map(int,sys.stdin.readline().split())
sky=list(list(sys.stdin.readline().rstrip()) for _ in range(h))
for i in range(h):
    for j in range(w):
        if sky[i][j] == 'c':
            sky[i][j] = 0
        else: 
            if j > 0 and sky[i][j-1] >= 0:
                sky[i][j] = sky[i][j-1]+1
            else:
                sky[i][j]=-1

for i in sky:
    print(*i)

