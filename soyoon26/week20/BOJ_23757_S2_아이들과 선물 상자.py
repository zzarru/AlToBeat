import heapq, sys
n, m = map(int,sys.stdin.readline().split())
p = []
c = list(map(int,sys.stdin.readline().split()))
for i in c:
    heapq.heappush(p,-i)
w = list(map(int,sys.stdin.readline().split()))
answer = 1
for j in w:
    x = heapq.heappop(p)
    x += j
    if x > 0:
        answer = 0
        break
    else:
        heapq.heappush(p,x)
print(answer)