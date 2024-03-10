import sys
N=int(sys.stdin.readline().rstrip())
graph=[[] for _ in range(N+1)]
for i in range(N-1):
    a,b=map(int,sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
Q=int(sys.stdin.readline().rstrip())
for q in range(Q):
    t,k=map(int,sys.stdin.readline().split())
    if t == 1:
        if len(graph[k])>1:
            print("yes")
        else:
            print("no")
    else:
        print("yes")