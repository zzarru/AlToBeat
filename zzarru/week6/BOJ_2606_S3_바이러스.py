from collections import deque

n = int(input()) # 컴퓨터의 개수
line = int(input()) # 연결된 상의 개수
network = [[] for _ in range(n+1)]
for _ in range(line):
    a, b = map(int, input().split())
    network[a].append(b)
    network[b].append(a)

# 큐 구현
def bfs(x):
    deq = deque([x])
    count = 0
    visited[x] = True
    while deq:
        node = deq.popleft()
        for next_node in network[node]:
            if not visited[next_node]:
                visited[next_node] = True
                deq.append(next_node)
                count += 1

    return count

visited = [False for _ in range(n+1)]
print(bfs(1))