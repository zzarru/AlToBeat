# BOJ 13023 G5 ABCDE

"""
친구 다섯명이 연속할 필요가 없음
문제에서 적힌거는 친구 다섯명의 index가 연속해야하는 것 처럼 해놓고..;;
각 node마다 똑같이 반복해서 dfs를 돌리면 되는데
백트래킹을 약간 추가해서 다음 노드 방문 전에 방문 해제를 해줘야 함
"""

n, m = map(int, input().split())
relations = [[] for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    relations[a].append(b)
    relations[b].append(a)


def dfs(start, friends):
    global answer
    if len(friends) == 5:
        answer = 1
        return

    for node in relations[start]:
        if not visited[node]:
            visited[node] = 1
            dfs(node, friends + [node])
            visited[node] = 0


answer = 0
visited = [0] * n
for i in range(n):
    visited[i] = 1
    dfs(i, [i])
    visited[i] = 0
    if answer:
        break

print(answer)
