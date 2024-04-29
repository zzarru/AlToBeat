'''
다익스트라는 최단비용을 찾는다.
그럼 기준점이 필요할것이다. 그래서 해당 기준점을 시작으로
탐색을 진행한다. 일단 큐에 넣어서 다음 진행할 곳을 계속해서
찾는건 BFS와 비슷하다 하지만 여기선 방문배열이 따로 필요하지 않다.
거리상으로 경쟁력이 사라지면 큐에 넣지 않기때문

1. 어떤 노드를 방문했다면
2. 해당 노드에 대한 거리의 기록 distance 배열과 
현재 노드까지 탐사를 통해 혹시나 개선될지도 모를 기록 until_node를 비교한다.
3. 혹여나 개선의 여지가 없다면 큐에 추가없이 바로 다음 탐사를 진행
4. 개선의 여지가 보일경우 큐에 추가할 다음노드와 기록 until_node를 queue에 추가한다.
'''

from collections import deque

N, M, K, X = map(int,input().split())

distance = [ 1e9 for i in range(N+1)]
distance[X] = 0
# 틀렸습니다를 마주하고 생각해보니 경곗값일거라고 느꼈고 문제에서
# 자기 자신도 생각하라는 언지가 있었다.
graph = [ [] for _ in range(N+1)]
answer = []

for _ in range(M):
    A, B = map(int,input().split())
    graph[A].append((B,1))

queue = deque()
queue.append((X,0))


while queue:
    node, until_node = queue.popleft()
    if until_node > distance[node]:
        continue

    for next, from_node_to_next in graph[node]:
        cost = until_node + from_node_to_next

        if cost < distance[next]:
            distance[next] = cost
            queue.append((next, cost))

for i in range(N+1):
    if distance[i] == K:
        answer.append(i)

if answer:
    for i in answer:
        print(i)
else:
    print(-1)

