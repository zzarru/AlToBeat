# BOJ 18243 S1 Small World Network

"""
각 노드에 대해서 bfs를 진행한다.
모든 노드를 방문할 수 있고, 거리가 6 이하라면 Small World
아니라면 Big World를 출력하고 종료한다.
"""

from collections import deque


def bfs(start):
    """
    거리가 6 이하인 노드들을 탐색
    :param start: 시작 노드
    :return: 모든 노드를 방문할 수 있다면 1, 아니면 0
    """
    q = deque([(start, 0)])
    visited = [0] * (n + 1)
    visited[start] = 1
    while q:
        current, depth = q.popleft()
        for node in relations[current]:
            if not visited[node]:
                if depth < 6:
                    visited[node] = 1
                    q.append((node, depth + 1))

    return all(visited[1:])


n, k = map(int, input().split())
relations = [[] for _ in range(n + 1)]
for _ in range(k):
    a, b = map(int, input().split())
    relations[a].append(b)
    relations[b].append(a)

for i in range(1, n + 1):
    result = bfs(i)
    if not result:
        print('Big World!')
        exit(0)

print('Small World!')
