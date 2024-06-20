from collections import defaultdict
import sys
sys.setrecursionlimit(10**8)
n, m, l = map(int,input().split())
graph = [[0 for _ in range(m)] for _ in range(n)]
visited = [[0 for _ in range(m)] for _ in range(n)]
for _ in range(l):
    i, j = map(int,input().split())
    graph[i-1][j-1] = 1

s_dict = defaultdict(int)

di = [0,1,0,-1]
dj = [1,0,-1,0]

flag = 1
def dfs(i,j):
    visited[i][j] = 1
    s_dict[flag] += 1
    #전역변수이므로 참조만 가능하고 수정은 불가 flag += 1을 여기서 할 수 없음
    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]
        if 0 <= ni < n and 0 <= nj < m :
            if not visited[ni][nj] and graph[ni][nj]:
                dfs(ni,nj)

for i in range(n):
    for j in range(m):
        if not visited[i][j] and graph[i][j]:
            dfs(i,j)
            flag += 1

print(max(list(s_dict.values())))



