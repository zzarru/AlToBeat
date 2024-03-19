'''

이 문제는 델타탐색과, DFS 또는 BFS를 활용해서 좌표에 정보를 색인 할 수 있는지 알아보는 문제였다.
문제에서는 배추가 심긴 곳의 좌표를 제공해주고, 해당 지점에서 인접한 곳은 한 벌레로
케어가 가능하기때문에 그곳을 방문처리해주고, 방문처리된 곳을 cur_index라는 변수로 색인해주었다.
거창하게 말해서 색인이지만, 그냥 전체좌표가 어떤 덩어리로 나뉘어지는지 확인하는 문제였다.


'''

tc = int(input())
for _ in range(tc):
    M, N, K = map(int,input().split()) # 행 열
    graph = [[0 for _ in range(M)] for _ in range(N)]
    visited = [[0 for _ in range(M)] for _ in range(N)]
    v = [] # 좌표정보를 넣을 리스트

    for _ in range(K):
        a, b = map(int,input().split())
        # 갑자기 일반 수학 좌표로 입력을 주기때문에
        # 뒤집어서 그래프에 넣어준다.
        graph[b][a] = 1
        v.append((b,a))

    cur_index = 1
    index = []

    def dfs(i,j):
        # 시작전에 이미 방문했거나, 혹은 배추가 없는 곳일 경우 사전에 차단
        if visited[i][j] or not graph[i][j]:
            return
        visited[i][j] = 1

        di = [0,0,-1,1]
        dj = [-1,1,0,0]

        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < N and 0 <= nj < M and not visited[ni][nj]:
                index.append(cur_index)
                dfs(ni,nj)

    for i,j in v:
        dfs(i,j)
        cur_index += 1

    print(len(set(index)))
