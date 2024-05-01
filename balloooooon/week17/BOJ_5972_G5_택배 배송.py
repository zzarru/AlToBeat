from collections import deque
start=1
V,E=map(int,input().split())
route=[]
for _ in range(E):
    route.append(list(map(int,input().split())))
INF=int(1e9)
graph=[[] for _ in range(V+1)]

distance = [INF]*(V+1)

for info in route:
    graph[info[0]].append((info[1],info[2]))#양방향
    graph[info[1]].append((info[0],info[2]))

queue = deque()
queue.append((start, 0)) #시작노드와 그거리는 0
distance[start] = 0

while queue:
    node, dis =queue[0] #전노드의 distance가 dis
    queue.popleft()

    if distance[node] < dis:
        continue
    for info in graph[node]:
        cost = dis + info[1]
        if cost < distance[info[0]]:
            distance[info[0]] = cost
            queue.append((info[0],cost))