from collections import defaultdict
import sys
sys.setrecursionlimit(10**8)
s_dict = defaultdict(int)

n, m = map(int,input().split())

graph = [ list(map(int,input().split())) for _ in range(n)]
visited = [ [0 for _ in range(m)] for _ in range(n)]

di = [0,1,0,-1]
dj = [1,0,-1,0]
index = 1
def dfs(i,j):
    visited[i][j] = index
    s_dict[index] += 1
    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]
        if 0 <= ni < n and 0 <= nj < m :
            if not visited[ni][nj] and graph[ni][nj]:
                dfs(ni, nj)

for i in range(n):
    for j in range(m):
        if not visited[i][j] and graph[i][j]:
            dfs(i, j)
            index += 1

value_list = list(s_dict.values())

if value_list:
    print(len(s_dict))
    print(max(value_list))
else:
    print(0)
    print(0)