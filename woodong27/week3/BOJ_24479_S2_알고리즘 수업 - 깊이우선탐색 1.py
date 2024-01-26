# BOJ 24479 S2 알고리즘 수업 - 깊이 우선 탐색 1

"""
어제 푼 너비 우선 탐색 1 과 같은 원리다.
재귀를 사용해서 dfs를 구현하고
오름차순으로 진행할 수 있도록 nodes들을 정렬해주었다.
"""

import sys

# 파이썬 기본 재귀 횟수 제한때문에 recursion error 발생
# -> 재귀 횟수 추가
sys.setrecursionlimit(10**6)

enter = sys.stdin.readline

n, m, r = map(int, enter().strip().split())

nodes = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v = map(int, enter().strip().split())
    nodes[u].append(v)
    nodes[v].append(u)

nodes = [sorted(node) for node in nodes]

visited = [0] * (n + 1)
result = [0] * (n + 1)
count = 1

def dfs(current):
    global visited, result, count
    result[current] = count
    count += 1
    for node in nodes[current]:
        if not visited[node]:
            visited[node] = 1
            dfs(node)


visited[r] = 1
dfs(r)

for i in range(1, n + 1):
    print(result[i])
