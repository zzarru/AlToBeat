'''
1. 어찌됐든 leaf에서 leaf사이의 거리 중 최대거리를 구하면된다는
접근을 통해서 먼저 leaf들을 모조리 dfs를 돌려 거리를 구했으나 메모리초과
2. 그렇다면 애초에 이진트리니까 가망이 없는 leaf를 조기에 걸러내자는 취지로 반복문을 돌렸으나 이 또한 메모리초과
3. 그러면 대체 방법이 뭘까 하다가 인터넷을 찾아보니 처음에 루트에서 가장 먼 노드를 구하고 거기서 다시 dfs를 돌려서 나온
거리가 최대가 된다는 증명을 발견, 하지만 솔직히 이유는 모름 일단 확인후 적용 그런데 또 메모리 초과
4. 거리를 저장해놓은 배열이 잘못된걸까 싶어 해당 배열을 딕셔너리로 바꾸니 겨우 통과

증명이 필요한 이론이 있다는 것 자체가 매우 괘씸하고, 다시 보고싶지않은 문제이다

'''

import sys
sys.setrecursionlimit(int(1e6))

n = int(input())
dist = {}
graph = [[] for i in range(n+1)]
visited = [0 for i in range(n+1)]
for _ in range(n-1):
    a, b, v = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
    dist[(a,b)] = v
    dist[(b,a)] = v
answer = [0 for i in range(n+1)]
def dfs(cur, dis):
    visited[cur] = 1
    for nxt in graph[cur]:
        if not visited[nxt]:
            nxt_dis = dis + dist[(cur,nxt)]
            answer[nxt] = nxt_dis
            dfs(nxt, nxt_dis)

dfs(1,0)

start = answer.index(max(answer))
visited = [0 for i in range(n+1)]
dfs(start,0)
print(max(answer))


