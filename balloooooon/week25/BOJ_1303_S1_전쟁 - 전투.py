m, n = map(int,input().split())
graph = [ list(input()) for _ in range(n)]
visited = [ [ 0 for _ in range(m)] for _ in range(n)]

di = [0,1,0,-1]
dj = [1,0,-1,0]

member = home = away = 0

def membership(i,j, team):
    visited[i][j] = 1
    global member
    member += 1
    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]
        if 0 <= ni < n and 0 <= nj < m and not visited[ni][nj] and graph[ni][nj] == team:
            membership(ni,nj,team)

for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            member = 0
            team = graph[i][j]
            membership(i,j,team)
            
            if team == 'W':
                home += member**2
            else:
                away += member**2

print(home,away)