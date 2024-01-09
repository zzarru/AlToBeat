N, M = map(int, input().split())

matrix_1 = [list(map(int, input().split())) for _ in range(N)]
matrix_2 = [list(map(int, input().split())) for _ in range(N)]

ans = [list(0 for i in range(M)) for l in range(N)]

for x in range(N):
    for y in range(M):
        ans[x][y] = matrix_1[x][y] + matrix_2[x][y]

for _ in range(N):
    print(*ans[_])
