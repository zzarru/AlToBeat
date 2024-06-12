import sys
sys.setrecursionlimit(10**5)

v, w, start = map(int,input().split())
graph = [ [] for _ in range(v+1)]
visited = [0 for _ in range(v+1)]
order = [0 for _ in range(v+1)]
for _ in range(w):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
for temp in graph:
    temp.sort()

cur_order = 1

def dfs(cur):
    global cur_order
    visited[cur] = 1
    order[cur] = cur_order
    cur_order += 1
    for nxt in graph[cur]:
        if not visited[nxt]:
            dfs(nxt)
dfs(start)
for i in order[1:]:
    print(i)