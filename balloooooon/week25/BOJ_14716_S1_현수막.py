import sys
sys.setrecursionlimit(10**6) # 재귀깊이를 설정하지 않으니 RecursionError가 났다.

n, m = map(int,input().split())
graph = [ list(map(int,input().split())) for _ in range(n) ]
visited = [ [0 for _ in range(m)] for _ in range(n) ]

di = [0,1,1,1,0,-1,-1,-1]
dj = [1,1,0,-1,-1,-1,0,1]

def dfs(i, j, id):
    visited[i][j] = 1

    for k in range(8):
        ni = i + di[k]
        nj = j + dj[k]
        if 0 <= ni < n and 0 <= nj < m and not visited[ni][nj] and graph[ni][nj]:
            dfs(ni,nj, id)

answer = 0

for i in range(n):
    for j in range(m):
        if not visited[i][j] and graph[i][j]:
            dfs(i,j,answer)
            answer += 1

print(answer)