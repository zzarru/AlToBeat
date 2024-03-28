'''
이 문제는 수위에 따라서 건물들이 물에 잠기는데, 잠기는건물이 더 산발적으로 분포해있으면 안전지대로써 더 경쟁력?있어진다고 한다.
그래서 각 수위를 한단계씩 올려서 dfs를 통해 각 안전지역 후보를 탐색하고 수위별 안전지대 갯수를 더 높은 값으로 갱신해주어서 답을 찾아주었다.
도중에 수위가 높아져버려서 아틀란티스가 되는경우 곧바로 탐색을 종료시켜 불필요한 시간낭비를 없애주었다.
'''


import sys
sys.setrecursionlimit(10**8)

N = int(input())
graph = []
max_building_level = 0
answer = 0
water_level = 0

for _ in range(N):
    temp = list(map(int,input().split()))
    max_building_level = max(max(temp), max_building_level)
    graph.append(temp)



def dfs(i,j, temp_water_level):
    visited[i][j] = 1
    di = [0,0,1,-1]
    dj = [1,-1,0,0]

    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]
        if 0 <= ni < N and 0 <= nj < N and graph[ni][nj] > temp_water_level and not visited[ni][nj]:
            # 해당 좌표가 존재해야하고, 일단 안전한지도 판별하고, 방문한적도 없어야함
            dfs(ni,nj, temp_water_level)


while 1:
    cnt = 0
    visited = [ [ False for _ in range(N)] for _ in range(N) ]
    for i in range(N):
        for j in range(N):
            if graph[i][j] > water_level and not visited[i][j]:
                dfs(i, j, water_level)
                cnt += 1

    answer = max(answer, cnt) # 정답을 갱신
    water_level += 1
    if water_level >= max_building_level: # 수위가 높아져서 아틀란티스가 되었는가?
        break

print(answer)



