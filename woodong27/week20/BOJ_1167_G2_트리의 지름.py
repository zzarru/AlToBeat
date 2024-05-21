# BOJ 1167 G2 트리의 지름

"""
트리에서 임의의 노드의 최대거리에 있는 노드는 트리의 지름의 양 끝점 중 하나다.
-> 해결법
1. 아무 노드에서 한 번 탐색해서 지름의 끝점 하나를 찾는다.
2. 그 노드에서 다시 탐색해서, 가장 먼 거리를 찾는다.
"""


import sys


def dfs(start_):
    global visited
    for next_, distance in tree[start_]:
        if visited[next_] == -1:
            visited[next_] = visited[start_] + distance
            dfs(next_)


if __name__ == '__main__':
    enter = sys.stdin.readline
    v = int(enter())
    tree = [[] for _ in range(v + 1)]
    for _ in range(v):
        node, *edges = map(int, enter().strip().split())
        for i in range(0, len(edges), 2):
            if edges[i] == -1:
                break
            tree[node].append([edges[i], edges[i+1]])

    visited = [-1] * (v + 1)
    visited[1] = 0
    dfs(1)
    start = visited.index(max(visited))

    visited = [-1] * (v + 1)
    visited[start] = 0
    dfs(start)
    answer = max(visited)

    sys.stdout.write(f'{answer}\n')
