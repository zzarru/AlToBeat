'''
부모노드를 확인하는 가장 편한 방법으로 문제에서 1이라는 노드를 루트노드로 잡고 BFS를 해주었다.
'''

from collections import deque

N = int(input())

graph = [ [] for i in range(N+1)]

for _ in range(N-1):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

queue = deque()
queue.append(1)

visited = [0 for i in range(N+1)]
answer = [0 for i in range(N+1)]
visited[1] = 1

while queue:
    par = queue.popleft()
    for child in graph[par]:
        if not visited[child]:
            queue.append(child)
            visited[child] = 1
            # print(par, child)
            answer[child] = par

for i in range(2,N+1):
    print(answer[i])
