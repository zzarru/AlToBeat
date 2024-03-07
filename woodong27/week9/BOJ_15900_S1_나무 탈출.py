# BOJ 15900 S1 나무 탈출

"""
성원이가 먼저 게임을 시작하기 때문에
말을 움직일 수 있는 횟수가 홀수여야 승리할 수 있다.

dfs를 통해 각 노드의 루트에서부터의 깊이를 구해주고
원소가 한 개인 노드(리프노드)의 깊이의 합(=말 이동 횟수)가 홀수면 승리할 수 있다.

*
python3으로 제출하니까 시간초과 떠서
pypy3로 제출하니까 recursion limit 10 ** 6 일떄 메모리 초과 발생
최악의 경우 재귀 횟수 50만 번 이라서 50만으로 설정하니까 통과
"""

import sys

sys.setrecursionlimit(5 * 10 ** 5)
enter = sys.stdin.readline

n = int(enter().strip())
nodes = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, enter().strip().split())
    nodes[a].append(b)
    nodes[b].append(a)


def count_depth(current):
    for node in nodes[current]:
        if not visited[node]:
            visited[node] = 1
            depth[node] = depth[current] + 1
            count_depth(node)


depth = [0] * (n + 1)
visited = [0] * (n + 1)
root = 1
visited[root] = 1
count_depth(root)

count = 0
for i in range(2, n + 1):
    if len(nodes[i]) == 1:
        count += depth[i]

answer = 'Yes' if count % 2 else 'No'
print(answer)
