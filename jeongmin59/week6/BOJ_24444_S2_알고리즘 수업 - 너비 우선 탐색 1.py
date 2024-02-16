# 24444_알고리즘 수업 - 너비 우선 탐색 1
'''
- N개의 정점과 M개의 간선으로 구성된 무방향 그래프가 주어짐
- 정점 번호 1~N번, 가중치 1
- R에서 시작해서 방문할 경우 방문 순서 출력
- 인접 정점은 오름차순으로 방문
- M개 줄에 간선 정보 u v 주어짐
'''

from collections import deque
import sys
input = sys.stdin.readline

N, M, R = map(int, input().split())
graph = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)     # 방문 여부 확인

for i in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

for i in range(N + 1):      # 오름차순 정렬
    graph[i].sort()


def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = 1
    cnt = 2

    while queue:
        v = queue.popleft()

        for i in graph[v]:  # 시작 노드와 연결된 노드만 방문
            if visited[i] == 0:
                queue.append(i)
                visited[i] = cnt
                cnt += 1


bfs(graph, R, visited)

for i in range(1, N + 1):
    print(visited[i])
