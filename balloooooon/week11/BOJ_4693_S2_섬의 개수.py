import sys
sys.setrecursionlimit(10**8)
input=sys.stdin.readline

while True:

    n,m=map(int,input().rstrip().split()) #열 행
    if n==0 and m==0:
        break
    graph=[list(map(int,input().rstrip().split())) for _ in range(m)]
    visited=[[0 for _ in range(n)] for _ in range(m)]

    di=[-1,-1,-1,0,1,1,1,0]
    dj=[-1,0,1,1,1,0,-1,-1]
    cnt=0

    def dfs(start1,start2):
        global cnt
        if graph[start1][start2]==0:
            return

        elif visited[start1][start2]==1:
            return
        visited[start1][start2]=1
        cnt += 1

        def search(current1,current2):
            for k in range(8):
                ni = current1 + di[k]
                nj = current2 + dj[k]
                if 0<=ni<m and 0<=nj<n:
                    if graph[ni][nj] == 1 and not visited[ni][nj]:
                        visited[ni][nj] = 1
                        search(ni, nj)
        search(start1,start2)

    for i in range(m):
        for j in range(n):
            dfs(i,j)
    print(cnt)