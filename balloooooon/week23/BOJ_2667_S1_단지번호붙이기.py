from collections import defaultdict
n = int(input())

graph = [list(map(int,input())) for _ in range(n)]
visited = [[0 for _ in range(n)] for _ in range(n)]
id_dict = defaultdict(int)

def dfs(i,j, id):
    visited[i][j] = id
    id_dict[id] += 1
    di = [0,1,0,-1]
    dj = [1,0,-1,0]

    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]
        if 0 <= ni < n and 0 <= nj < n and not visited[ni][nj] and graph[ni][nj]:
            dfs(ni,nj,id)

id = 1

for i in range(n):
    for j in range(n):
        if not visited[i][j] and graph[i][j]:
            dfs(i,j,id)
            id += 1

towns = sorted(list(id_dict.values()))

print(len(towns))
for town in towns:
    print(town)