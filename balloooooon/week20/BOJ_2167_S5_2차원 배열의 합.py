m, n = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(m)]

N = int(input())
for _ in range(N):
    ma, na, mb, nb = map(int,input().split())
    answer = 0
    for i in range(ma-1, mb):
        for j in range(na-1, nb):
            answer += graph[i][j]
    print(answer)