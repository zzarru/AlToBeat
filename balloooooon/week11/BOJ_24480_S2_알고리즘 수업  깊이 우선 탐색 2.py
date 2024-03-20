import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline
def dfs(start):
    visited[start]=True
    global cnt
    cnt += 1
    cnt_lst[start]=cnt

    for next in graph[start]:
        if not visited[next]:
            dfs(next)

N, M, R= map(int,input().split())
a=[]

for i in range(M):
    a.append(list(map(int,input().split())))
cnt=0

cnt_lst=[0 for _ in range(N+1)]
visited=[0 for _ in range(N+1)]
graph=[[] for _ in range(N+1)]

for i in a:
    graph[i[0]].append(i[1])
    graph[i[1]].append(i[0])
# for _ in range(M):
#     a, b = map(int, sys.stdin.readline().split(' '))
#     graph[a].append(b)
#     graph[b].append(a)
    
for i in graph:
    i.sort(reverse=1)
dfs(R)
for i in range(1,N+1):
    print(cnt_lst[i])