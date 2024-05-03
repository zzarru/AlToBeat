from collections import deque

N = int(input())
distance = [ 10e9 for _ in range(N+1)]
graph = [[] for _ in range(N+1)]
tc = int(input())
for _ in range(tc):
    A, B, cost = map(int,input().split())
    graph[A].append((B,cost))

start, end = map(int,input().split())

queue = deque()
queue.append((start,0))
distance[start] = 0

while queue:
    node, until_node = queue.popleft()

    if distance[node] < until_node:
        continue

    for next, to_next in graph[node]:
        cost = until_node + to_next
        if cost < distance[next]: #실수로 여기에 등호를 넣어서 메모리초과를 맛보았다
            distance[next] = cost
            queue.append((next,cost))

answer = distance[end]
print(answer)