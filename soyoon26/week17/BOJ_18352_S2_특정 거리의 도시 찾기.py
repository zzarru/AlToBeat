import sys, heapq
n,m,k,x=map(int,sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
inf = int(1e9)
distance = [inf]*(n+1)
for i in range(m):
    s,e = map(int,sys.stdin.readline().split())
    graph[s].append(e)
def dstr(start):
    q=[]
    heapq.heappush(q,(0,start))
    distance[start] = 0
    while q:
        dist,now = heapq.heappop(q)
        if dist > distance[now]:
            continue
        for i in graph[now]:
            cost = dist + 1
            if cost < distance[i]:
                distance[i] = cost
                heapq.heappush(q,(cost,i))
dstr(x)
answer = 0
for i in range(1,n+1):
    if distance[i] == k:
        print(i)
        answer = 1
if answer == 0:
    print(-1)
