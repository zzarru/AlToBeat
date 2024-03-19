'''
전형적인 BFS, DFS를 할 수 있는지 묻는 문제로
기본개념 정리를 해주는 듯한 문제였다.
'''

N, M, V = map(int,input().split())

graph = [[] for i in range(N+1)]

for _ in range(M):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

for branch in graph:
    branch.sort()

answer_dfs = []
answer_bfs = []
def dfs(n):
    visited = [ 0 for _ in range(N+1)]
    answer_dfs.append(n)

    def search(cur):
        visited[cur] = 1
        for nxt in graph[cur]:
            if not visited[nxt]:
                answer_dfs.append(nxt)
                search(nxt)
    search(n)

def bfs(n):
    visited = [ 0 for _ in range(N+1)]
    queue = []

    def search(cur):
        visited[cur] = 1
        answer_bfs.append(cur)
        queue.append(cur)

        while queue:
            cur = queue.pop(0)
            for nxt in graph[cur]:
                if not visited[nxt]:
                    visited[nxt] = 1
                    queue.append(nxt)
                    answer_bfs.append(nxt)

    search(n)


bfs(V)
dfs(V)

print(*answer_dfs)
print(*answer_bfs)
