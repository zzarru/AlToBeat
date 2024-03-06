import sys
sys.setrecursionlimit(int(1e5))
'''
어제와 동일하게 하려니까 런타임에러가 났는데, 참고했던 최소공통조상 알려준
곳에서 재귀깊이로 인해 런타임에러가 뜰 수도 있다고 경고했었다. 잘못하면 오랫동안 삽질할뻔 했다.
'''


tc = int(input())

for _ in range(tc):
    n = int(input())
    graph = [ [] for _ in range(n+1) ]
    parent = [0] * (n+1)
    visited = [0] * (n+1)
    d = [0] * (n+1)
    root = 0

    for _ in range(n-1):
        p, c = map(int,input().split())
        parent[c] = p
        graph[p].append(c)
        graph[c].append(p)

    for i in range(1,n+1):
        if parent[i]:
            continue
        else: #자신의 부모?가 없는게 루트노드이니까 충실히 이행해주었다...
            root = i
            break

    def dfs(cur, depth):
        d[cur] = depth
        visited[cur] = 1
        for nxt in graph[cur]:
            if not visited[nxt]:
                dfs(nxt, depth + 1)

    dfs(root,0)

    m, n = map(int,input().split())

    def lca(a,b):

        while d[a] != d[b]:
            if d[a]>d[b]:
                a = parent[a]
            else:
                b = parent[b]

        while a != b:
            a = parent[a]
            b = parent[b]

        return a

    print(lca(m,n))