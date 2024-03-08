import sys
sys.setrecursionlimit(int(1e5))

n= int(input())
graph = [[] for _ in range(n+1)]
p = [0 for _ in range(n+1)] # 자식을 인덱스로, 부모를 값으로 저장하는 배열
d = [0 for _ in range(n+1)] # 해당 노드의 깊이를 기록한 배열
visited = [0 for _ in range(n+1)]

for _ in range(n-1):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
    # p[b] = a 양방향이기때문에 여기서 조사하면 엉뚱한 부모자식관계가 형성될 수 있다.

def dfs(cur, depth):
    visited[cur] = 1
    d[cur] = depth
    for nxt in graph[cur]:
        if not visited[nxt]:
            p[nxt] = cur
            dfs(nxt, depth + 1)

def lca(a,b):
    while d[a] != d[b]:
        if d[a] > d[b]:
            a = p[a]
        else:
            b = p[b]

    while a != b:
        a = p[a]
        b = p[b]

    return a

dfs(1,0)

m = int(input())

for _ in range(m):
    x, y = map(int,input().split())
    print(lca(x,y))