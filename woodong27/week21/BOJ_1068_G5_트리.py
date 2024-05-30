# BOJ 1068 G5 트리

"""
삭제하고자 하는 노드를 tree의 node 목록에서 지우고 dfs를 실행하면 된다.
탐색 중 자식노드가 없는 노드를 만나면 리프노드이므로 answer에 1을 더해준다.
"""

import sys


def dfs(start):
    global answer
    if not tree[start]:
        answer += 1
        return
    for node in tree[start]:
        dfs(node)


if __name__ == '__main__':
    enter = sys.stdin.readline
    n = int(enter())
    parents = list(map(int, enter().split()))
    delete = int(enter())
    
    tree = [[] for _ in range(n)]
    root = 0
    for i in range(n):
        if parents[i] == -1:
            root = i
        elif i != delete:
            tree[parents[i]].append(i)
            
    answer = 0
    if delete != root:
        dfs(root)
        sys.stdout.write(f'{answer}\n')
