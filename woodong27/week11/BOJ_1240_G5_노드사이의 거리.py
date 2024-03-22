# BOJ 1240 G5 노드사이의 거리

"""
골드티어 문제기는 한데.. dfs만 할 줄 알면 쉽게 풀 수 있는 문제
노드사이의 거리를 저장하기 위한 count변수를 추가해서
dfs를 돌리면 된다.
"""

n, m = map(int, input().split())
tree = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    node1, node2, distance = map(int, input().split())
    tree[node1].append((node2, distance))
    tree[node2].append((node1, distance))


def dfs(s, e, count):
    if s == e:
        print(count)
    for node, distance in tree[s]:
        if not visited[node]:
            visited[node] = 1
            dfs(node, e, count + distance)


for _ in range(m):
    start, end = map(int, input().split())
    visited = [0] * (n + 1)
    visited[start] = 1
    dfs(start, end, 0)
