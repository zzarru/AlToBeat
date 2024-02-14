# 너비 우선 탐색을 공부하면서 미로를 만드는데 쓰인다고 했었던게 떠올라서 활용해보았다.

n,m = map(int,input().split())

graph = [input() for i in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]

start = (0,0) # 시작위치
queue = [start] # 큐에 넣어주고
visited[start[0]][start[1]] = 1 # 시작위치 방문처리

# 델타 탐색을 위한 방향벡터 설정
di = [0,0,-1,1]
dj = [-1,1,0,0]

while queue:
    cur_i, cur_j = queue.pop(0)
    for k in range(4):
        ni = cur_i + di[k]
        nj = cur_j + dj[k]

        if 0 <= ni < n and 0 <= nj < m and int(graph[ni][nj]) and not visited[ni][nj]:
            # 다음 노드가 범위내에 있고,
            # 다음 노드가 지나갈 수 있는 길이고
            # 방문한 적이 없다면

            queue.append((ni,nj))
            # 큐에 좌표정보를 넣어준다.

            visited[ni][nj] += visited[cur_i][cur_j] + 1
            # 방문확인에 거리 정보까지 넣어두기

answer = visited[n-1][m-1] # 목표지점까지의 최단거리를 확인
print(answer)

