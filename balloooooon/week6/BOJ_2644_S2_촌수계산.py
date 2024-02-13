# 이 문제를 풀면서 예전에 트리에 관련해서 너무너무 편협한 생각을 가지고 있었다고 느꼈다.
# 우리는 항상 트리구조를 1부터 시작하는 정직한 구조를 생각하는데
# 이 문제는 '촌수'를 확인하기에 start를 어디로 하느냐에 따라 트리를 다르게 생각할 수 있다.
# 보통은 할아버지, 아버지, 아들 이런 순서가 맞지만
# 생각을 뒤집어서 아들이 제일 위에 있는 트리구조라고도 생각해볼 수 있다.
# 그림으로 그린걸 90도 150도 280도 회전시켜서 생각해보는 유연한 사고를 가져보자
def bfs(start, end, graph):
    visited = [False for i in range(len(graph))]
    start = (start,1) # 노드이외에 해당 노드까지의 상대적인 거리를 추가로 정보를 넣는다.
    queue = [start]
    visited[start[0]] = True
    while queue:
        current, dis = queue.pop(0)
        for nxt in graph[current]:
            if not visited[nxt]:
                queue.append((nxt, dis+1))
                visited[nxt] = True
                if nxt == end:
                    return dis # start에서 end로 탐색시 해당 거리 출력
    return -1 # 만일 start에서 end로 탐색을 못했다면 온전히 -1 출력

n = int(input())

start, end = map(int,input().split())

m = int(input())

graph = [[] for i in range(n+1)]

for _ in range(m):
    par, child = map(int,input().split())
    graph[par].append(child)
    graph[child].append(par)

answer = bfs(start, end ,graph)
print(answer)