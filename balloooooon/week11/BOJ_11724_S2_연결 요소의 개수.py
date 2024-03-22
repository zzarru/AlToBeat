'''
모든 정점에서 DFS를 실행은 해본다.
단, 해당 정점을 '방문한적 없을 때만'
그러면 연결되있는 그래프 끼리는 방문배열에 동일한 정수로 기록을 해둔다.
CHECK라는 변수는 그런 그래프가 몇개인지 확인시켜준다.
'''

N, M = map(int,input().split())

graph = [ [] for _ in range(N+1) ]
visited = [ 0 for _ in range(N+1) ]

check = 0

def dfs(cur):
    visited[cur] = check

    for nxt in graph[cur]:
        if not visited[nxt]:
            dfs(nxt)

for _ in range(M):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

for idx in range(1,N+1):
    if not visited[idx]:
        check += 1
        dfs(idx)

print(check)

