# 백준 24444 S2 알고리즘 수업 - 너비 우선 탐색 1

"""
input()을 사용하니까 시간초과가 뜨던게
sys.stdin.readline()을 사용하니까 해결됐다.
일단 시간초과가 뜨면 sys입력으로 바꿔보자

기본적인 bfs문제인데
다음 방문할 노드들을 오름차순으로 q에 넣어야 하기 때문에
bfs를 돌리기 전에 각 node들을 정렬해주는 과정을 거쳤다.
"""

from collections import deque
import sys

enter = sys.stdin.readline

n, m, r = map(int, enter().strip().split())

nodes = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v = map(int, enter().strip().split())
    nodes[u].append(v)
    nodes[v].append(u)

nodes = [sorted(node) for node in nodes]

result = [0] * (n + 1)
visited = [0] * (n + 1)
visited[r] = 1
q = deque([r])
count = 1
while q:
    current = q.popleft()
    result[current] = count
    count += 1
    temp = []
    for node in nodes[current]:
        if not visited[node]:
            q.append(node)
            visited[node] = 1

for i in range(1, n + 1):
    print(result[i])
