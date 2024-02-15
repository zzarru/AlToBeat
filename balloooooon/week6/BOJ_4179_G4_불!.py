'''
어제의 미로찾기를 풀고나서 이 문제가 눈에 들었는데, 희박한 정답률을 보고 솔직히 풀지 않을까도 생각을 했었다.
하지만 뭔가 머리에 아이디어가 번뜩여서 접근을 해보았는데, 시간초과의 늪에 빠졌었고 12초 에서 0.001초로 경감시켰음에도
통과되지 않는 것에 이 문제의 출처 사이트에 접근해서 TC를 적용시키고 내가 얼마나 우매했는지 납득했다.

문제를 풀면서 깨우친것은
방문했음을 조사하는 배열을 주인공과, 불 따로 설정하는 것

BFS는 맞지만 내가 한번 움직였다고 다음에 바로 불을 움직이는게 아닌
한 사이클 단위로 움직일것
이게 무슨 애기냐면
얘를 들어 내가 4방향 움직인것을 큐에 넣었다고 치자 그렇다면 먼저 동쪽으로 움직인 케이스에 대해
다음 케이스를 큐에 넣을 것이고 방문배열도 최신화 할 것이다
그리고 불이 움직이는 것에 BFS를 돌리면?
그럼 서, 북, 남에 대한 케이스는 불에 먹히고 만다
'내가 한번 움직였을때 갈 수 있는 모든 가능성단위'로 BFS를 해야한다.

그리고 방문배열은 '신'이다
중복방지로 시간 절약이 말도 안되게 된다.


'''

import sys
input = sys.stdin.readline
n,m = map(int,input().rstrip().split())

graph = []
FireList = []

for i in range(n):
    temp = list(input().rstrip())
    graph.append(temp)
    for j in range(m):
        if temp[j] == 'F':
            FireList.append((i,j))
        if temp[j] == 'J':
            start = (i,j)


# 델타 탐색을 위한 방향벡터 설정
di = [0,0,-1,1]
dj = [-1,1,0,0]

obstacle = ['#', 'F']
answer = 0
def bfs(start, FireList):
    visited = [[False for _ in range(m)] for _ in range(n)]
    visited2 = [[False for _ in range(m)] for _ in range(n)]


    queue = [start]  # 큐에 넣어주고
    visited[start[0]][start[1]] = 1  # 시작위치 방문처리
    while queue:
        now = len(queue)
        for i in range(now):
            cur_i, cur_j = queue.pop(0)
            for k in range(4):
                ni = cur_i + di[k]
                nj = cur_j + dj[k]
                '''
                장외로 갈 수 있다면 탈출 가능성을 제시한 것이다. 난 0미만의 경우를 빼먹어서 한번 틀렸다.
                '''
                if (ni<0 or n<=ni or m<=nj or nj<0) and graph[cur_i][cur_j]=='J':
                    answer = visited[cur_i][cur_j]
                    return answer

                if 0 <= ni < n and 0 <= nj < m and graph[cur_i][cur_j]=='J' and not graph[ni][nj] in obstacle and not visited[ni][nj] :

                    '''
                    다음 노드가 범위내에 있고,
                    다음 노드가 지나갈 수 있는 길이고
                    방문한 적이 없다면
                    '''

                    queue.append((ni,nj))
                    graph[ni][nj] = 'J'

                    visited[ni][nj] += visited[cur_i][cur_j] + 1
                    # 방문확인에 거리 정보까지 넣어두기

        temp = [] #불에 대해 bfs를 돌리기위해 만든 배열
        for i,j in FireList:
            for k in range(4):
                ni = i + di[k]
                nj = j + dj[k]
                if 0 <= ni < n and 0 <= nj < m and graph[ni][nj] != '#' and not visited2[ni][nj]:
                    visited2[ni][nj] = 1
                    graph[ni][nj] = 'F'
                    temp.append((ni,nj))
        FireList = temp

answer = bfs(start, FireList)

if answer:
    print(answer)
else:
    print('IMPOSSIBLE')



