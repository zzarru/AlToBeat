from collections import defaultdict
import sys
sys.setrecursionlimit(10**8)
n, m = map(int,input().split())
a = b = 0
graph = []
for i in range(n):
    temp = list(input())
    if 'I' in temp:
        a = i
        b = temp.index('I')
    graph.append(temp)

visited = [ [0 for _ in range(m)] for _ in range(n)]

di = [0,1,0,-1]
dj = [1,0,-1,0]

answer = 0
def dfs(i,j):
    global answer
    visited[i][j] = 1
    if graph[i][j] == 'P':
        answer += 1
    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]
        if 0 <= ni < n and 0 <= nj < m :
            if not visited[ni][nj] and (graph[ni][nj] == 'O' or graph[ni][nj] == 'P'):
                dfs(ni,nj)

dfs(a,b)

if answer:
    print(answer)
else:
    print('TT')


