# BOJ 11725 S2 트리의 부모 찾기

import sys

sys.setrecursionlimit(10 ** 9)
enter = sys.stdin.readline

"""
root노드는 1이라고 지정되어있음
현재 노드가 다음 노드의 부모가 되기때문에
방문한 다음 노드의 visited에는 현재 노드를 넣어주면 됨
출력은 루트노드인 1번위 부모를 제외하고 2번 부터 출력하면 됨

RecursionError가 발생해서 
recursionlimit을 늘려줬음
"""

n = int(enter().strip())

tree = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    node1, node2 = map(int, enter().strip().split())
    tree[node1].append(node2)
    tree[node2].append(node1)

visited = [0] * (n + 1)


def find_parent(start):
    for node in tree[start]:
        if not visited[node]:
            visited[node] = start
            find_parent(node)


root = 1
find_parent(root)
print(*visited[2:], sep='\n')
